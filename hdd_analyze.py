from commands import *

path = Path.combine("Volumes", "Untitled", "Users")

bad_ext = JsonList("bad.json")
good_ext = JsonList("good.json")

class State:
    files_count = 0
    folders_count = 0
    total_size = 0  # bytes
    finished = False
    extensions = []
    last_path = None

    running_threads = []

    bench = Bench()

    @classmethod
    def add_files(self, count):
        self.files_count += count

    @classmethod
    def add_folders(self, count):
        self.folders_count += count

    @classmethod
    def add_size(self, count):
        self.total_size += count

    @classmethod
    def add_thread(self, path):
        self.running_threads.append(path)

    @classmethod
    def remove_thread(cls, path):
        cls.running_threads.pop(cls.running_threads.index(path))


def analyze_files(root, files):
    State.add_thread(root)
    for file in files:
        filepath = Path.combine(root, file)

        # cleanup logic
        if "-large" in File.get_extension(file):
            File.move(filepath, Str.rreplace(filepath, "-large", "", 1))
            filepath = Str.rreplace(filepath, "-large", "", 1)
        # end cleanup logic

        ext = File.get_extension(file).lower()

        # cleanup logic
        if ext in bad_ext:
            File.delete(filepath, quiet=False, no_sleep=True)
            continue
        if file.lower() in ["thumbs.db", "desktop.ini"]:
            File.delete(filepath, quiet=False, no_sleep=True)
            continue
        # end cleanup logic

        State.last_path = filepath
        State.add_size(File.get_size(filepath))
        if ext not in State.extensions:
            State.extensions.append(ext)
    State.remove_thread(root)


def analyzer():
    try:
        for root, dirs, files in OS.walk(path):
            State.add_files(len(files))
            State.add_folders(len(dirs))

            if not dirs and not files:
                Dir.delete(root)

            therad = MyThread(analyze_files, args=(root, files))
            therad.start()
    except Exception as e:
        print(e)
    finally:
        State.finished = True


def printer():
    while (not State.finished) or (State.running_threads):
        # Console.clean()
        print(f"{Time.dotted()[:19+3]}> Drive {path1}: "
              f"scanned {round(State.total_size/1024/1024/1024, 2)}Gb, "
              f"{State.files_count} files, "
              f"{State.folders_count} dirs.{newline}"
              f"{len(State.extensions)} unique extensions.{newline}"
              f"{' '.join(Console.fit('Last file:', State.last_path))}{newline}"
              f"analyze_files threads: {len(State.running_threads)}{newline}"
              f"Time passed: {round(State.bench.get(), 2)}s{newline}")
        Time.sleep(1)


t = Threading()
t.add(analyzer)
t.add(printer)
t.start(wait_for_keyboard_interrupt=True)

try:
    while not State.finished or State.extensions:
        print("no exts")
        Time.sleep(0.5)
        # clean State.extensions
        for ext in bad_ext:
            try:
                State.extensions.pop(State.extensions.index(ext))
            except:
                pass
        for ext in good_ext:
            try:
                State.extensions.pop(State.extensions.index(ext))
            except:
                pass
        # end clean extensions

        for ext in State.extensions:
            if ext not in bad_ext and not ext in good_ext:
                if CLI.get_y_n(f"Remove {ext}"):
                    bad_ext.append(ext)
                else:
                    good_ext.append(ext)
except:
    print()
    print(bad_ext)
    print(good_ext)
    raise
