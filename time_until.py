from commands import *
from pyfiglet import Figlet
from datetime import timedelta

figlet = f = Figlet(font="term", justify="center", width=Console.width())


figlet_mode = "figlet" in OS.args
# fonts = Str.nl(File.read("pyfiglet_fonts.txt").strip())


def now():
    return Time.datetime()


ends = []

for arg in OS.args[1:]:
    ends.append(arg)

if not ends:
    print("No times given, exit")

end_times = []

last_end_time = Time.datetime(year=1970)

for end in ends:

    end = Str.get_integers(end)

    try:
        new_end_time = Time.datetime(hour=end[0], minute=end[1], second=0)
    except IndexError:
        continue

    while True:
        if new_end_time < last_end_time:
            new_end_time = new_end_time + timedelta(days=1)
        else:
            break

    end_times.append(new_end_time)

    last_end_time = new_end_time

# debug
# for end_time in end_times:
# print(end_time)
# debug END

end_times.sort()

# debug
# print()
# for end_time in end_times:
# print(end_time)
# debug END

# cnt = Json("time_until_cnt.json")
# if not isinstance(cnt.string, int):
# cnt.string = 0

if not figlet_mode:
    Console.clean()

while True:
    if figlet_mode:
        Console.clean()
    rebuild = True
    result = ""
    previous_end_time = None
    current_end_time = None
    for cnt_end_time, end_time in enumerate(end_times):
        time = now()

        if end_time < time:
            continue

        if current_end_time is None:
            current_end_time = end_time
            i = cnt_end_time - 1
            previous_end_time = end_times[cnt_end_time - 1]
            if i < 0:
                previous_end_time = end_times[-1] - Time.delta(24 * 3600)

        rebuild = False

        seconds = int((end_time - time).total_seconds())
        human_readable = Time.human_readable(seconds)

        until = f"{end_time.hour:02}:{end_time.minute:02}"

        if end_time.day != time.day:
            until = f"{end_time.day:02}.{end_time.month:02} {until}"

        if figlet_mode:
            # font = "minecraft"
            font = "minecraft_condensed"

            f = Figlet(font=font, justify="center", width=Console.width())

            result += f.renderText(f"{human_readable} until {until}").rstrip() + newline
        else:
            human_readable = human_readable.replace("m", "")
            human_readable = human_readable.replace("h", "")
            human_readable = human_readable.replace("s", "")
            human_readable = human_readable.replace(" ", "")
            result += f"{human_readable} {end_time.minute:02}|"

    # progressbar
    # diff_total = int(Time.delta(end_times[0], end_times[-1]))
    # diff_now = int(Time.delta(Time.datetime(), end_times[-1]))

    if rebuild:
        for cnt, end_time in enumerate(end_times):
            end_times[cnt] = end_time + Time.delta(24 * 3600)
        continue

    if previous_end_time == current_end_time:
        previous_end_time -= timedelta(days=1)

    diff_total = int(Time.delta(previous_end_time, current_end_time))
    diff_now = int(Time.delta(Time.datetime(), current_end_time))
    
    diff_percent = f"{100 - diff_now / diff_total * 100:.2f}"

    if not figlet_mode:
        diff_percent = f"{result}{diff_percent.replace('.', '')}"

    progressbar = CLI.progressbar(diff_now, diff_total, diff_percent + ("%" if figlet_mode else ""), reverse=True)

    if figlet_mode:
        output = result.rstrip() + newline + Console.fit(progressbar)[0]
        print(output, end="", flush=True)
    else:
        output = Console.fit(progressbar, reverse=True)[0]
        # print(f"\r{output}", end="", flush=True)  # have cursor at the end of the line to show the end of progressbar
        print(f"{output}")

    if figlet_mode:
        Time.sleep(1)
    else:
        Time.sleep(Random.integer(1, 10), verbose=False)
