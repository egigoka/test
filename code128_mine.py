#! python3
import code128

code128.image("Hello World").save("Hello World.png")  # with PIL present

with open("Hello World.svg", "w") as f:
        f.write(code128.svg("Hello World"))

import tempfile
import win32api
import win32print

filename = tempfile.mktemp (".txt")
open (filename, "w").write ("This is a test")
win32api.ShellExecute (
  0,
  "print",
  filename,
  #
  # If this is None, the default printer will
  # be used anyway.
  #
  '/d:"%s"' % win32print.GetDefaultPrinter (),
  ".",
  0
)
