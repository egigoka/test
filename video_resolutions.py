from moviepy.editor import *
from commands import *

folder = OS.args[1]

bad_extesnions = [".py"]

good_sizes = [[1920, 1080]]

bad_sizes = []

for root, dirs, files in OS.walk(folder):
    for file in files:
        ext = File.get_extension(file)
        if ext in bad_extesnions:
            pass

        path = Path.combine(root, file)

        clip = VideoFileClip(path) 
        size = clip.size

        color = "yellow"
        if size in bad_sizes:
            color = "red"
        elif size in good_sizes:
            color = "green"
        
        Print.colored(*Console.fit(size, path), color)
