from commands import *

debug = "--debug" in OS.args


cache = JsonDict("cache/progress.json")

try:
    end_goal = cache["end_goal"]
except KeyError:
    end_goal = CLI.get_integer("end goal")
    cache["end_goal"] = end_goal
    cache.save()

try:
    if not isinstance(cache["progress"], dict):
        cache["progress"] = {}
except KeyError:
    cache["progress"] = {}

cache["progress"] = Dict.sorted_by_key(cache["progress"])

while True:
    try:
        progress = CLI.get_integer("current progress")
    except KeyboardInterrupt:
        OS.exit(0)
    
    time = Time.stamp()
    cache["progress"][time] = progress
    cache.save()

    if len(cache["progress"]) == 1:
        continue
    
    begin_progress = 10 if len(cache["progress"]) >= 10 else len(cache["progress"])

    progress_items = list(cache["progress"].items())
    begin = progress_items[-begin_progress]
    end = progress_items[-1]
    begin_time = begin[0]
    end_time = end[0]
    begin_progress = begin[1]
    end_progress = end[1]
    
    delta_time = end_time - float(begin_time)
    delta_progress = end_progress - int(begin_progress)
    
    # Check if delta_time is zero to avoid division by zero error
    if delta_time == 0:
        progress_per_second = 0
    else:
        progress_per_second = abs(delta_progress / delta_time)

    if delta_progress < 0:
        progress_per_second *= 2
    
    goal_diff = end_goal - end_progress
    
    # Check if progress_per_second is zero to avoid division by zero error
    if progress_per_second == 0:
        print("never will end")
        print()
        continue
    else:
        seconds_to_goal = goal_diff / progress_per_second

    end_delta = Time.delta(seconds_to_goal)
    end_datetime = Time.datetime() + end_delta

    if debug:
        Print.debug(f"{begin_time=}", f"{end_time=}", f"{begin_progress=}", f"{end_progress=}",
                    f"{delta_time=}", f"{delta_progress=}", f"{progress_per_second=}", f"{goal_diff=}",
                    f"{end_goal=}", f"{seconds_to_goal=}", f"{end_delta=}", f"{end_datetime=}")

    time_formatted = " " + Time.human_readable(end_delta)

    if time_formatted == " ":
        time_formatted = "stantly"
    
    print("will end in " + str(end_datetime) + ", in" + time_formatted)
    print()
