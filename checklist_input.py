from commands import *

tasks = '''ГрупповаяФК_EAN_ITF__OLD
ГрупповаяФК_ITF
ЭтикеткаOld
ГрупповаяФК_EAN
ГрупповаяФК
МакетСписокИнформационныхЗнаков
ШаблонКолбасныйЦех
ЭтикеткаБезДатыИСрока
УзкаяНаБатон
ТолькоДаты
Этикетка
ГрупповаяФК_EAN_ITF
ТолькоДатыИВес
ТолькоДатыВакуум
УпакованоПодВакуумомМГС'''
tasks = Str.nl(tasks)
subtasks = '''весовой товар
фиксированный вес
штрихкод короткий
штрихкод длинный'''
subtasks = Str.nl(subtasks)
Time.sleep(5, verbose=True)


for task in tasks:
    Time.sleep(0.1)
    copy(task)
    Keyboard.hotkey("ctrl", "v", verbose=True)
    Time.sleep(0.1)
    Keyboard.hotkey("enter", verbose=True)
    Time.sleep(0.1)
    Keyboard.hotkey("tab", verbose=True)
    Time.sleep(0.1)

    for subtask in subtasks:
        copy(subtask)
        Keyboard.hotkey("ctrl", "v", verbose=True)
        Time.sleep(0.1)
        Keyboard.hotkey("enter", verbose=True)
        Time.sleep(0.1)

    Keyboard.hotkey("shift", "tab", verbose=True)
    Time.sleep(0.1)
