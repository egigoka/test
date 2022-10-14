from commands import *

bad_extensions = [".dbf", ".py", ".pdf", ".ini", ".mst", ".msi", ".cab", ".exe", ".dt", ".epf", ".docx", ".mxl", ".doc",
                  ".xlsx", ".xls", ".xmind", ".inf", ".dll", ".ico", ".cdd", ".ogg", ".wav", ".btn", ".psd", ".png",
                  ".pptx", ".ppt", ".erf", ".cfe", ".efd", ".dcf", ".cf", ".st", ".html",
                  ".css", ".js", ".xml", ".sel", ".url", ".swf", ".valog", ".vbs", ".cdx",
                  ".xsd", ".txt", ".загружено", ".reg", ".sys", ".cat", ".bak", ".cmd",
                  ".db", ".jpg", ".sql", "", ".csv", ".cer", ".sav", ".bat", ".1c_rep",
                  ".au3", ".chm", ".gw", ".htm", ".onetoc2", ".vrp", ".log", ".rtf", ".one",
                  ".1cd", ".sh", ".mht", "", ".grs", ".xd", ".ttf", ".woff", ".woff2", ".eot", ".iml", 
                  ".pyc", ".md", ".json"]
skipped_folders = ["./1С Предприятие 8/1C8.2_videokurs_Krotov_Roman_Report_1C_2013/AutoPlay/Videos/",
                   "./1С Предприятие 8/Применение агрегатов, индексов, итогов для повышения быстродействия/Лекции/Лекции/files/",
                   "./1С Предприятие 8/Программирование в системе 1С Предприятие 8.3/7-1С-Предприятие 8.3. Средства интеграции и обмена данными/Файлы",
                   "./1С_обработки",
                   "./1С Предприятие 8/Профессия 1C-разработчик [2020]/1С-разработчик с нуля до PRO/01.Обзор системы «1СПредприятие»/1.1 Материалы к уроку/",
                   "./1С Предприятие 8/Профессия 1C-разработчик [2020]/1С-разработчик с нуля до PRO/13.Язык запросов SQL/",
                   "./Web_1c/[УЦ-3] WEB-курс Применение агрегатов, индексов, итогов для повышения быстродействия/[УЦ-3] WEB-курс Применение агрегатов, индексов, итогов для повышения быстродействия/Лекции/files",
                   "./Web_1c/[УЦ-3] WEB-курс Применение агрегатов, индексов, итогов для повышения быстродействия/Лекции/files",
                   "./Web_1c/[УЦ-3] WEB-курс Программирование в стандартных типовых решениях системы 1СПредприятие 8.3 (2018)/files",
                   "./Web_1c/[УЦ-3] Web-сервисы (SOAP), HTTP-сервисы, oData (автоматический REST-сервис) (2017)/files"]
# debug
# bad_extensions.append(".zip")
# bad_extensions.append(".rar")
# bad_extensions.append(".7z")

cache = JsonDict("cache_calculate_length.json")


def get_duration(filename):
    # print(filename)
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    duration = clip.duration
    # fps = clip.fps
    # width, height = clip.size
    return duration


out = {}

errors = 0

roots = 0
for root, dirs, files in OS.walk('.'):
    roots += 1
    
cnt = 0
for root, dirs, files in OS.walk('.'):
    cnt += 1
    Print.rewrite(f"{CLI.wait_update(quiet=True)}{cnt} of {roots}", root)
    file_duration_total = 0

    for file in files:
        ext = File.get_extension(file).lower()

        root_in_skipped_folders = False
        for skipped_folder in skipped_folders:
            if root.startswith(skipped_folder):
                root_in_skipped_folders = True
        
        if ext in bad_extensions:
            continue

        filepath = Path.combine(root, file)
        
        if filepath in cache:
            file_duration_total += cache[filepath]
            continue

        try:
            print(CLI.wait_update(quiet=True), end="\r")
            current_file_duration = get_duration(filepath)
            file_duration_total += current_file_duration
            cache[filepath] = current_file_duration
            cache.save()
        except (OSError, KeyError):
            if not root_in_skipped_folders:
                Print.colored(filepath, f"{ext=}", "red")
                errors += 1
                if errors > 10:
                    exit(1)
        

    if file_duration_total != 0:
        # Print.colored(root, file_duration_total, "green")
        toot = root.split("/")
        # print(toot)
        key = toot[1]

        if key in ["1С Предприятие 8", "Павел Чистов", "СКД", "Web_1c", "Библиотека стандартных подсистем"]:
            key += backslash + toot[2]

        # print(key)
        try:
            out[key] += int(file_duration_total)
        except KeyError:
            out[key] = int(file_duration_total)

Print.rewrite()

cnt = 0
for key in sorted(out, key=out.get, reverse=False):
    cnt += 1
    value = out[key]

    dir_ = key
    duration = value

    h = duration / 3600
    s = int((h - int(h)) * 3600)

    m = s / 60
    s = int((m - int(m)) * 60)

    Print.colored(dir_, f"{int(h)}h {int(m)}m {int(s)}s", 
                  "on_white" if cnt % 2 == 0 else "on_black", 
                  "black" if cnt % 2 == 0 else "white")

total_duration = 0
for duration in out.values():
    total_duration += duration

h = total_duration / 3600
s = int((h - int(h)) * 3600)

m = s / 60
s = int((m - int(m)) * 60)

print(f"TOTAL: {int(h)}h {int(m)}m {int(s)}s, {cnt} folders")
