from commands import *
mins = Int.from_to(0,60, to_str=True)
hours_start = Int.from_to(8, 11, to_str=True)
hours_end = Int.from_to(14,16, to_str=True)
len_mins = Int.from_to(15,120)

min_start = Random.item(mins)
hour_start = Random.item(hours_start)
min_end = int(min_start)  + Random.item(len_mins)
hour_end = int(hour_start) + int(min_end/60)
min_end = min_end % 60
print(hour_start, ":", min_start, "-", str(hour_end).zfill(2), ":", str(min_end).zfill(2))

min_start = Random.item(mins)
hour_start = Random.item(hours_end)
min_end = int(min_start) + Random.item(len_mins)
hour_end = int(hour_start) + int(min_end/60)
min_end = min_end % 60
print(hour_start, ":", min_start, "-", str(hour_end).zfill(2), ":", str(min_end).zfill(2))