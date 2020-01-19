from commands import *
import os
import sys

print("init")

old_working_dir = Path.working()
working_dir = "/Users/mac/Documents/fckng photoshop"

Path.set_working(working_dir)
os.system("ulimit -n 4096")
gif_path = Path.combine(working_dir, "png_to_gif.gif")

if "gif" in sys.argv:
    print("creating gif")

    File.delete(gif_path)


    import imageio
    import os

    path = working_dir
    image_folder = os.fsencode(path)

    filenames = []

    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith('.png'):
            filenames.append(filename)

    filenames.sort()  # this iteration technique has no built in order, so sort the frames

    images = list(map(lambda filename: imageio.imread(filename), filenames))

    imageio.mimsave(gif_path, images, duration = 0.03)  # modify the frame duration as needed

if "zip" in sys.argv:
    print("compressing gif")

    out = Console.get_output(Path.combine(old_working_dir, "gifsicle-mac"),
                             "-O3", "--lossy=200", "-o", Path.combine(working_dir, "apple-checkrain.gif"), gif_path)

    File.delete(gif_path)

    print(out)

print("Done")