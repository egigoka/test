﻿#! python3
# -*- coding: utf-8 -*-
import pyautogui
from commands7 import *
import tripleclick


class Arguments:
    for arg in sys.argv:
        batch_unload = False
        if arg == "batch":    # рейсы
            batch_unload = True
        test = False
        if arg == "test":
            test = True
        single_unload = False
        if arg in ["o","one","onebyone","obo"]:
            single_unload = True


class State:
    move_duration = 0.1
    sleep_before_click = 0.1
    sleep_before_locate = 0.1
    ctrl_a_sleep = 3
    buttons_pics_folder = Path.extend("C:", "shares", "scripts", "tripleclick", "buttonpics")
    quiet = False
    get_img_name_quiet = True


class Click:
    @staticmethod
    def click(button, position):
        time.sleep(State.sleep_before_click)
        if position:
            pyautogui.click(x=position[0],y=position[1],button=button)
        else:
            pyautogui.click(button=button)
        if not State.quiet:
            print("click mouse " + button)
    
    @classmethod
    def right(cls,position=None):
        cls.click(button='right',position=position)

    @classmethod
    def left(cls,position=None):
        cls.click(button='left',position=position)


Timer = Bench

def get_img_name(*name_shards):
    if len(name_shards[0]) == 0:
        raise IndexError("first name shard is empty")
    #debug_print("name_shards",name_shards,"len(name_shards)",len(name_shards),"len(name_shards[0])",len(name_shards[0]))
    imgs = []
    for file in Dir.contain(State.buttons_pics_folder):
        file_is_good = True
        for name_shard in name_shards:
            #print("name_shard",name_shard,"not in","file",file,name_shard not in file)
            if name_shard not in file:
                file_is_good = False
        if file_is_good:
            imgs += [file]
    if len(imgs) == 1:
        if not State.quiet and not State.get_img_name_quiet:
            print("found image", imgs[0], "with shards", name_shards)
        return Path.extend(State.buttons_pics_folder, imgs[0])
    else:
        raise IndexError("found " + str(len(imgs)) + " buttons pics by " + str(name_shards) + " shards: " + str(imgs))


def move(x, y=None, x2=None, y2=None, duration=State.move_duration, tween=pyautogui.easeInOutQuad):
    if isinstance(x, tuple):
        if len(x) == 2:
            y = x[1]
            x = x[0]
        elif len(x) == 4:
            y = x[1]
            x2 = x[2]
            y2 = x[3]
            x = x[0]
    if x2 and y2:
        x,y = pyautogui.center((x,y,x2,y2))
    if not State.quiet:
        print("moved mouse to", x, y)
    pyautogui.moveTo(x, y, duration=duration, tween=tween)

def locate(*name_shards, safe=False):  # seconds  # todo multiple locate
    time.sleep(State.sleep_before_locate)
    name = get_img_name(*name_shards)
    filename = os.path.split(name)[1]
    position = pyautogui.locateOnScreen(name)
    if (position is None) and not safe:
        raise IndexError("not located " + filename + " ")
        sys.exit(1)
    if not State.quiet:
        message = "not located " + filename
        if position:
            message = substring(message, before="not ") + " on " + str(position)
        print(message)
    return position           


def wait_locate(*name_shards, every=1, timeout=60, safe=False):
    timeout_reached = False
    position = None
    Timer.start()
    while not timeout_reached and not position:
        time.sleep(every)
        position = locate(*name_shards, safe=True)
        timeout_reached = Timer.end(quiet=True) > timeout
    if timeout_reached and not position and not safe:
        raise RuntimeError("timeout " + str(timeout) + " reached while searching for " + str(name_shards))
    return position

def hotkey(*args):
    pyautogui.hotkey(*args)

class Scroll:     

    def scroll(value, up):
        value = int(value)
        if not up:
            value = 0-value
        pyautogui.vscroll(clicks=value)
        print("scrolled", value)

    @classmethod
    def up(cls, value=100):
        cls.scroll(value, up=True)
    
    @classmethod
    def down(cls, value=100):
        cls.scroll(value, up=False)


class Open:

    class Solvo:
        class Menu:
            class Documents:
                @staticmethod
                def documents():
                    Click.left(move(locate("документы", "бел")))
                @classmethod
                def orders(cls):
                    cls.documents()
                    Click.left(move(wait_locate("заказы", "бел", timeout=10)))
                    wait_locate("progressbarstill", every=0.1, timeout=60)
                @classmethod
                def shipments(cls):
                    cls.documents()
                    Click.left(move(locate("отправки", "бел", timeout=10)))
                    wait_locate("progressbarstill", every=0.1, timeout=60)

    @staticmethod
    def solvo():
        opened = None
        opened = locate("solvomini")
        if not opened:
            Click.left(move(locate("SOLVO")))

try:
    
    if Arguments.test:
        def main():
            pass
            # Open.solvo()

    if Arguments.single_unload:
        def main():
            while True:
                Open.solvo()                                                                # открыть солво
                Open.Solvo.Menu.Documents.orders()                                          # открыть окно заказы
                workarea = wait_locate("светлозел", every=1, timeout=30)                    # найти зелёную рабочую область
                Click.left(move(workarea))                                                  # нажать левой кнопкой по рабочей области
                hotkey('ctrl', 'a')                                                         # выделить всё
                time.sleep(State.ctrl_a_sleep)                                              # подождать, пока всё выделится
                dropdown = None                                                             # меню не выпало
                while not dropdown:                                                         # пока не выпадет меню:
                    Click.right(move(workarea))                                                 # нажать правой кнопкой по рабочей области
                    dropdown = wait_locate("команды", "бел", every=0.1, timeout=10, safe=True)  # найти Команды...
                Click.left(move(dropdown))                                                  # нажать на Команды...
                Click.left(move(wait_locate("отгрузитьбелая", every=0.1, timeout=10)))      # нажать на Отгрузить
                wait_locate("progressbarempty", every=15, timeout=600)                      # подождать, пока отгрузится
            
    
    if Arguments.batch_unload:    # рейсы
        def main():
            Open.solvo()
            Open.Solvo.Menu.Documents.shipments()
            while True:
                position = None
                while not position:
                    try:
                        position = locate("готов", "к", "отгрузке", "син")
                    except IndexError as err:
                        print (err)
                        try:
                            position = locate("готов", "к", "отгрузке", "бел")
                        except IndexError as err:
                            print (err)
                            move(locate("готовкотгрузкевыделенная"))
                            Scroll.up()
                move(position)
                Click.right()
                move(wait_locate("команды", "бел", every=0.1, timeout=10))
                move(wait_locate("отгрузитьбелая", every=0.1, timeout=10))
                Click.left()
                
                ok_position = None
                while not ok_position:
                    try:
                        ok_position = locate("окбелая")
                    except IndexError as err:
                        print (err)
                        try:
                            time.sleep(2)
                            ok_position = locate("progressbarstill")
                        except IndexError as err:
                            print(err)
                move(ok_position)
                Click.left()
except KeyboardInterrupt:
    print("^C")

#def main():
#     while True:
#         value = 100
#         pyautogui.vscroll(clicks=value)
#         print("scrolled", value)






tripleclick.main = main
tripleclick.start()