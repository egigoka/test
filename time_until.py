from commands import *
from pyfiglet import Figlet
from datetime import timedelta

figlet = f = Figlet(font="term", justify="center", width=Console.width())


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

    new_end_time = Time.datetime(hour=end[0], minute=end[1], second=0)

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

while True:
    Console.clean()
    rebuild = True
    result = ""
    for end_time in end_times:
        time = now()

        # Print.debug(f"{end_time=}")
        # Print.debug(f"{time=}")

        if end_time < time:
            continue

        rebuild = False

        seconds = int((end_time - time).total_seconds())
        # Print.debug(f"{seconds=}")
        human_readable = Time.human_readable(seconds)
        # Print.debug(f"{human_readable=}")

        # font = Random.item(fonts)
        # try:
        # font = fonts[cnt.string]
        # except IndexError:
        # cnt.string = 0
        # font = fonts[cnt.string]
        # font = "minecraft"
        font = "minecraft_condensed"

        # cnt.string += 1
        # cnt.save()

        # print(figlet.renderText(f"{font} {cnt.string}/{len(fonts)}"))
        # print(figlet.renderText(f"{font}"))

        f = Figlet(font=font, justify="center", width=Console.width())

        until = f"{end_time.hour:02}:{end_time.minute:02}"

        if end_time.day != time.day:
            until = f"{end_time.day:02}.{end_time.month:02} {until}"

        result += f.renderText(f"{human_readable} until {until}").rstrip() + newline

        # if seconds <= 0:
        #   Console.blink()
        #   break

    # progressbar
    diff_total = int(Time.delta(end_times[0], end_times[-1]))
    diff_now = int(Time.delta(Time.datetime(), end_times[-1]))
    human_readable_total = Time.human_readable(diff_total)
    human_readable_now = Time.human_readable(diff_now)
    # print(f"{diff_total=} {diff_now=} {human_readable_total=} {human_readable_now=}")
    diff_percent = 100 - int(diff_now / diff_total * 100)
    progressbar = CLI.progressbar(diff_now, diff_total, f"{diff_percent}%", reverse=True)

    # print(result.rstrip(), end="", flush=True)

    print(result.rstrip() + newline + progressbar, end="", flush=True)

    if rebuild:
        for cnt, end_time in enumerate(end_times):
            end_times[cnt] = end_time + Time.delta(24 * 3600)
    # OS.exit(1)
    Time.sleep(1)
