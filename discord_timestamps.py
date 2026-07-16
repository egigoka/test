import re
from commands import paste, copy

data = paste()

match = re.search(r"(\d+)", data)
if match is None:
    raise ValueError(f"no timestamp found in clipboard: {data!r}")

ts = int(match.group(1))
style = "F"
style_match = re.search(r"<t:\d+:(\w)>", data)
if style_match:
    style = style_match.group(1)

timestamps = [f"{hour + 1}) <t:{ts + 3600 * hour}:{style}>" for hour in range(0, 24)]

result = "\n".join(timestamps)
print(result)
copy(result)
