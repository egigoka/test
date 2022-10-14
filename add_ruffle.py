import re
try:
    from commands import *
except ImportError:
    print("install commands with command 'pip3 install git+https://github.com/egigoka/commands")

htmls = 0
for root, dirs, files in OS.walk('.'):
    for file in files:
        if file.endswith(".html"):
            htmls += 1

cnt = 0
for root, dirs, files in OS.walk('.'):
    for file in files:
        if file.endswith(".html"):
            cnt += 1
            
            print(f"\n{cnt} of {htmls}")
            
            path = Path.combine(root, file)
            print("start", path)
            contents = File.read(path, auto_detect_encoding=10000000000)
            contents = contents.replace("</head>", "</head>\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>")
            while "\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>" in contents:
                contents = contents.replace("\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>", "\n<script src=\"https://unpkg.com/@ruffle-rs/ruffle\"></script>")
            
            heads = 0
            while len([m.start() for m in re.finditer('<head>', contents)]) > 1:
                contents = contents[:contents.rfind("<head>")] # cut off heads
                heads += 1
                print(f"\tcut {heads} heads")
            File.write(path, contents, mode="w")
            
            print("done", path)
input("press Enter to exit")
