#! python3
# -*- coding: utf-8 -*-
from commands8 import *

import pyautogui
sys.path.append(r"scripts/from_metropolis_work_mine/")
from solvounloader import *
#Time.timer(4)
#macOS.notification(title="spaceclicker", message="started")
#try:
#    cnt = 0
#    while cnt <=3000:
#        cnt+=1
#        pyautogui.hotkey("space")
#        time.sleep(0.15)
#except KeyboardInterrupt:
#    print(cnt)
#macOS.notification(title="spaceclicker", message="ended")
Time.timer(5)
macOS.notification(title="contact_creator_9000", message="started")
names=["Ronald", "Fan", "Gerald", "Jacob", "Bob", "Average"]
families=["Gloriousfucker", "Hater", "The_King", "Geometry"]

plus_pos = (1229, 748)
email_pos = (421, 469)
save_pos = (924, 604)
close_pos = (950, 383)

def get_fake_name(): return "fake.contact.bodoo."+str(Random.integer(1,1000))+"@gmail.com"

while True:
    Time.timer(2)
    Click.left(move(plus_pos))
    copypaste.copy(get_fake_name())
    hotkey('command',"v")
    Click.left(move(email_pos))
    copypaste.copy(get_fake_name())
    hotkey('command',"v")
    Click.left(move(save_pos))
    Time.timer(5)
    Click.left(move(close_pos))
