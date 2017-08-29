#! python3
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
        if arg in ["o","one","onebyone","obo"]:  # накладные
            single_unload = True
        single_unload_batch_support = False
        if arg in ["obozero", "onezero", "onebatch", "obobatch"]:  # накладные, привя
            single_unload_batch_support = True
        ctrl_v = False
        if arg in ["ctrlv"]:  # накладные, привя
            ctrl_v = True
        lo = False
        if arg in ["lo"]:  # накладные, привя
            lo = True


class State:
    move_duration = 0.5
    sleep_before_click = 0.1
    sleep_before_locate = 0.1
    before_ctrl_a_sleep = 0.5
    ctrl_a_sleep = 3
    buttons_pics_folder = Path.extend("T:", "buttonpics")
    quiet = False
    get_img_name_quiet = True


class Click:
    @staticmethod
    def click(button, position):
        sleep(State.sleep_before_click)
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

def locate_by_shards(*name_shards, safe=False, timer=False):  # seconds
    sleep(State.sleep_before_locate)
    name = get_img_name(*name_shards)
    filename = os.path.split(name)[1]
    position = pyautogui.locateOnScreen(name)
    if (position is None) and not safe:
        raise IndexError("not located " + filename + " ")
        sys.exit(1)
    if not State.quiet:
        message = "not located " + filename
        if position:
            message = Str.substring(message, before="not ") + " on " + str(position)
        elif timer:
            message += " timer " + str(Timer.get())
        print(message)
    return position


def locate(*names, safe=False, timer=False):
    output_position = None
    for name in names:
        output_position = locate_by_shards(name, safe=True, timer=timer)
        if output_position:
            return output_position
    if not safe:
        raise IndexError("nothing found from " + str(names) + " names")


def wait_locate(*names, every=1, timeout=60, safe=False):
    timeout_reached = False
    position = None
    Timer.start()
    while not timeout_reached and not position:
        sleep(every)
        position = locate(*names, safe=True, timer=True)
        timeout_reached = Timer.get() > timeout
    if timeout_reached and not position and not safe:
        raise RuntimeError("timeout " + str(timeout) + " reached while searching for " + str(names))
    return position

def hotkey(*args):
    pyautogui.hotkey(*args)
    print("pressed", str(args))

def sleep(seconds):
    if seconds >= 1:
        print("sleeping", seconds, "seconds")
    time.sleep(seconds)

def message(text, title='some window', button='oh no'):
    pyautogui.alert(text=text, title=title, button=button)

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


class Exceptions:
    class Check:
        @staticmethod
        def must_be_in_work():
            sleep(2)
            position = locate("mustbeinwork", safe=True)
            if position:
                message("LO must be in work!")


class Actions:
    def wait_for_done(fast=False):
        ok_position = None
        while not ok_position:
            try:
                ok_position = locate("окбелаяw7", "окбелаяw10")
            except IndexError as err:
                print (err)
                try:
                    sleep(2)
                    ok_position = locate("progressbaremptyw7", "progressbaremptyw10")
                    if not fast:
                        if ok_position:
                            ok_position_2 = wait_locate("окбелаяw7", "окбелаяw10", timeout=10, safe=True)
                            if ok_position_2:
                                ok_position = ok_position_2
                except IndexError as err:
                    print(err)
        move(ok_position)
        Click.left()


class Open:

    class Solvo:
        class Menu:
            class Documents:
                @staticmethod
                def documents():
                    Click.left(move(locate("документыбелаяw7", "документыбелаяw10")))
                @classmethod
                def orders(cls):
                    cls.documents()
                    Click.left(move(wait_locate("заказыбел", timeout=10)))
                    Actions.wait_for_done(fast=True)
                @classmethod
                def shipments(cls):
                    cls.documents()
                    Click.left(move(wait_locate("отправкибелая", timeout=10)))
                    Actions.wait_for_done(fast=True)
                @classmethod
                def lo(cls):
                    cls.documents()
                    Click.left(move(wait_locate("листыотбораw10", timeout=10)))
                    Actions.wait_for_done(fast=True)

    @staticmethod
    def solvo():
        opened = None
        opened = locate("solvomini", safe=True)
        if not opened:
            Click.left(move(locate("SOLVO")))
        else:
            move(opened)
            Click.left(move(opened))
            sleep(0.3)
            Click.left(move(opened))



try:

    if Arguments.test:
        def main():
            pass
            # Open.solvo()

    if Arguments.ctrl_v:
        def main():
            hotkey('ctrl', 'v')

    if Arguments.lo:
        def main():
            try:
                while True:
                    Open.solvo()                                                                # открыть солво
                    Open.Solvo.Menu.Documents.lo()                                              # открыть окно листов отбора
                    workarea = wait_locate("светлозел", every=1, timeout=30)                    # найти зелёную рабочую область
                    Click.left(move(workarea))                                                  # нажать левой кнопкой по рабочей области
                    sleep(1)                                                                    # подождать, пока всё выделится
                    dropdown = None                                                             # меню не выпало
                    while not dropdown:                                                         # пока не выпадет меню:
                        Click.right(move(workarea))                                                     # нажать правой кнопкой по рабочей области
                        dropdown = wait_locate("подтверждениелобел", every=0.1, timeout=10, safe=True)  # найти Подтверждение ЛО
                    Click.left(move(dropdown))                                                  # нажать Подтверждение ЛО
                    Click.left(move(wait_locate("окмаленькаяw10", "окмаленькаяw7", every=1, timeout=60)))        # нажать ОК
                    Exceptions.Check.must_be_in_work()
                    Actions.wait_for_done()
            except RuntimeError:
                Windows.lock()


    if Arguments.single_unload:
        def main():
            #try:
                while True:
                    Bench.start()
                    Open.solvo()                                                                    # открыть солво
                    Open.Solvo.Menu.Documents.orders()                                              # открыть окно заказы
                    workarea = wait_locate("светлозел", every=1, timeout=30)                        # найти зелёную рабочую область
                    Click.left(move(workarea))                                                      # нажать левой кнопкой по рабочей области
                    sleep(State.before_ctrl_a_sleep)
                    hotkey('ctrl', 'a')                                                             # выделить всё
                    sleep(State.ctrl_a_sleep)                                                       # подождать, пока всё выделится
                    dropdown = None                                                                 # меню не выпало
                    while not dropdown:                                                             # пока не выпадет меню:
                        Click.right(move(workarea))                                                     # нажать правой кнопкой по рабочей области
                        dropdown = wait_locate("команды...бел", every=0.1, timeout=10, safe=True)       # найти Команды...
                    Click.left(move(dropdown))                                                      # нажать на Команды...
                    Click.left(move(wait_locate("отгрузитьбелая", every=0.1, timeout=10)))          # нажать на Отгрузить

                    wait_locate("progressbaremptyw7", "progressbaremptyw10", every=15, timeout=600) # подождать, пока отгрузится
                    Bench.end()
            #except RuntimeError:
            #    Windows.lock()

    if Arguments.batch_unload:    # рейсы
        def main():
            Open.solvo()
            Open.Solvo.Menu.Documents.shipments()
            Click.left(move(wait_locate("светлозел", every=0.1, timeout=30)))
            hotkey('end')
            while True:
                Bench.start()
                position = None
                while not position:
                    try:
                        position = locate("готовкотгрузкесиняяw7", "готовкотгрузкесиняяw10", "готовкотгрузкебелаяw7", "готовкотгрузкебелаяw10")
                    except IndexError as err:
                        print (err)
                        move(locate("готовкотгрузкевыделеннаяw7", "готовкотгрузкевыделеннаяw10"))
                        if OS.windows_version == 10:
                            position_of_button = wait_locate("buttonup", every=0.1, timeout=30)
                            for i in Int.from_to(1,5):
                                sleep(0.1)
                                Click.left(move(position_of_button))
                        Scroll.up()
                move(position)
                Click.right()
                move(wait_locate("команды...белая", every=0.1, timeout=10))
                move(wait_locate("отгрузитьбелая", every=0.1, timeout=30))
                Click.left()
                Actions.wait_for_done()
                Bench.end()

    if Arguments.single_unload_batch_support:
        def main():
            while True:
                Open.solvo()
                Open.Solvo.Menu.Documents.orders()
                position = None
                debug_print("position", position)
                while not position:
                    try:
                        position = locate("собрансиняяw7", "собрансиняяw10", "собранзел")
                    except IndexError as err:
                        print(err)
                        move(wait_locate("светлозел", every=1, timeout=30))
                        Click.left()
                        Scroll.down(300)
                move(position)
                Click.right()
                move(wait_locate("перейтикэкранубелая", every=0, timeout=20))
                move(wait_locate("'отправки'белая", every=0, timeout=20))
                Click.left()
                Actions.wait_for_done()
                position_in_work = None
                position_in_work = locate("вработесин", "вработебел", safe=True)  # проверка рейса на собранность
                if position_in_work:
                    message('batch in work')
                    raise RuntimeError('batch in work')
                position = None
                while not position:
                    position = locate("собрансиняяw7", "собрансиняяw10", "собранбел")  # уже в отправках
                Click.right(move(position))
                move(wait_locate("команды...бел", every=0.5, timeout=20))
                move(wait_locate("подготовитькотгрузкебел", every=0.5, timeout=20))
                Click.left()
                Actions.wait_for_done()





except KeyboardInterrupt:
    print("^C")

#def main():
#     while True:
#         value = 100
#         pyautogui.vscroll(clicks=value)
#         print("scrolled", value)






tripleclick.main = main
tripleclick.start()
