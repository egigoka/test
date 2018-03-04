# Works with Microsoft Windows dos box
# Shows some use of WConio written by Chris Gonnerman

# Written by Priyend Somaroo
# Copyright (c) 2008 Vardaan Enterprises, www.vardaan.com

# Use and distribute freely.
# No liability for any use of this code will be accepted. Use is
# without any warranty whatsoever

# Requires the package WConio by Chris Gonnerman
# E-Mail : chris.gonnerman@newcenturycomputers.net
# Web : http://newcenturycomputers.net/projects/wconio.html

import WConio

#Store current attribute settings
old_setting = WConio.gettextinfo()[4] & 0x00FF

#Clear the screen
WConio.clrscr()

#Display something in low video
WConio.lowvideo()
WConio.cputs("Low video\r\n")

#Display something in high video
WConio.highvideo()
WConio.cputs("High video\r\n")

#Display something in normal video
WConio.normvideo()
WConio.cputs("Normal video\r\n")

#Display some text in color
WConio.textattr(WConio.LIGHTRED)
WConio.cputs("Light Red text\r\n")

#Display some more text in color
WConio.textattr(WConio.LIGHTBLUE)
WConio.cputs("Light BLUE text\r\n")

#leave a blank line - this shows you that print still works
print

#Set heading colour but using print
WConio.textattr(WConio.LIGHTGREEN)
print("Times table\r\n")

#Back to normal intensity for white
WConio.normvideo()

for i in range(12) :
  WConio.textattr(WConio.WHITE)
  a = "%2d * 2 = " % (i)
  WConio.cputs(a)
  WConio.textattr(WConio.YELLOW)
  a =  "%2d\r\n" % (i*2)
  WConio.cputs(a)

WConio.textattr(WConio.CYAN)
WConio.cputs("\n\nPress any key to end\r\n")

#Wait for a key to be pressed
WConio.getch()

#Retore old attribute settings
WConio.textattr(old_setting)
