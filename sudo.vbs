argc = WScript.Arguments.Count
set argv = WScript.Arguments
if argc < 1 then 
WScript.Echo "Usage: sudo <arg1 arg2 .. argN>"
WScript.quit
end if
dim str
for i = 1 to argc-1
str = str + " " + argv(i)
next
set objShell = CreateObject("Shell.Application") 
objShell.ShellExecute argv(0), str, "", "runas", 1