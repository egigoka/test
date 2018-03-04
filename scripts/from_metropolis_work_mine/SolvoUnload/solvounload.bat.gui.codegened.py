#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands7 import *  # mine commands
from solvounload import get_safe_time, get_current_time, settingsJsonFile as json_on_disk
from tkinter import *
root = Tk()
groups = [{"number": "1", "ko": "158", "lo": "329 %305 %269"},
          {"number": "2", "ko": "156", "lo": "268 %327"},
          {"number": "3", "ko": "73", "lo":"336 %337 %339"},
          {"number": "4", "ko": "125", "lo":"321 %322"},
          {"number": "5", "ko": "159", "lo": "335 %334"},
          {"number": "10", "ko": "121", "lo":"330 %331"},
          {"number": "fp", "ko": "143 %154", "lo": "332 %333"}, ]

def reloadJSON():
    File.backup(json_on_disk)
    global json_in_memory
    json_in_memory = Json.load(json_on_disk)
reloadJSON()

def savejson():
    json_in_memory["last_lo"] = last_lo_var.get()
    json_in_memory["last_batch"] = last_batch_var.get()
    json_in_memory["last_onebyone"] = last_onebyone_var.get()
    json_in_memory["kan_otb_time_1"] = ko_1_var.get()
    json_in_memory["kan_otb_note_1"] = ko_note_1_var.get()
    json_in_memory["kan_otb_time_2"] = ko_2_var.get()
    json_in_memory["kan_otb_note_2"] = ko_note_2_var.get()
    json_in_memory["kan_otb_time_3"] = ko_3_var.get()
    json_in_memory["kan_otb_note_3"] = ko_note_3_var.get()
    json_in_memory["kan_otb_time_4"] = ko_4_var.get()
    json_in_memory["kan_otb_note_4"] = ko_note_4_var.get()
    json_in_memory["kan_otb_time_5"] = ko_5_var.get()
    json_in_memory["kan_otb_note_5"] = ko_note_5_var.get()
    json_in_memory["kan_otb_time_10"] = ko_10_var.get()
    json_in_memory["kan_otb_note_10"] = ko_note_10_var.get()
    json_in_memory["kan_otb_time_fp"] = ko_fp_var.get()
    json_in_memory["kan_otb_note_fp"] = ko_note_fp_var.get()
    json_in_memory["note"] = note_var.get()
    check_buttons_and_colors()
    Json.save(json_on_disk, json_in_memory)
def inc_day(var):
    reloadJSON()
    new_date = json_in_memory[var][:2]
    new_date = str(int(new_date) + 1).zfill(2)
    if new_date == "32":
        new_month = str(int(json_in_memory[var][3:5]) + 1).zfill(2)
        new_date = "01." + new_month
    json_in_memory[var] = new_date + json_in_memory[var][len(new_date):]
    exec(var + "_var.set('" + json_in_memory[var] + "')")
    savejson()
def update_ko_1():
    if ko_note_1_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_1_var.set("пмммо")
    elif ko_note_1_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_1_var.set("пмммомМ")
    json_in_memory["kan_otb_note_1"] = ko_note_1_var.get()
    json_in_memory["kan_otb_time_1"] = get_current_time()
    ko_1_var.set(json_in_memory["kan_otb_time_1"])
    savejson()
ko_1_label = Label(root, text='1ГР %158 К.О. / %329 %305 %269 Л.О.')
ko_1_label.grid(row=0, column=0, sticky=E, rowspan=2)
ko_1_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_1_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_1_var = StringVar()
ko_1_var.set(json_in_memory["kan_otb_time_1"])
ko_1_entry = Entry(root, textvariable=ko_1_var, state=DISABLED)
ko_1_entry.grid(row=0, column=1, sticky=W+E+S+N, columnspan=1)
ko_1_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_1_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_1_var = StringVar()
ko_note_1_var.set(json_in_memory["kan_otb_note_1"])
ko_note_1_entry = Entry(root, textvariable=ko_note_1_var, state="normal")
ko_note_1_entry.grid(row=1, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_1_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_1_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_1_btn_r = 0
ko_1_btn = Button(root, height = 1, text = 'Update')
ko_1_btn.bind('<Button-1>', lambda x: update_ko_1())
ko_1_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_1_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_1_btn.grid(row=ko_1_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_2():
    if ko_note_2_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_2_var.set("пмммо")
    elif ko_note_2_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_2_var.set("пмммомМ")
    json_in_memory["kan_otb_note_2"] = ko_note_2_var.get()
    json_in_memory["kan_otb_time_2"] = get_current_time()
    ko_2_var.set(json_in_memory["kan_otb_time_2"])
    savejson()
ko_2_label = Label(root, text='2ГР %156 К.О. / %268 %327 Л.О.')
ko_2_label.grid(row=2, column=0, sticky=E, rowspan=2)
ko_2_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_2_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_2_var = StringVar()
ko_2_var.set(json_in_memory["kan_otb_time_2"])
ko_2_entry = Entry(root, textvariable=ko_2_var, state=DISABLED)
ko_2_entry.grid(row=2, column=1, sticky=W+E+S+N, columnspan=1)
ko_2_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_2_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_2_var = StringVar()
ko_note_2_var.set(json_in_memory["kan_otb_note_2"])
ko_note_2_entry = Entry(root, textvariable=ko_note_2_var, state="normal")
ko_note_2_entry.grid(row=3, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_2_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_2_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_2_btn_r = 2
ko_2_btn = Button(root, height = 1, text = 'Update')
ko_2_btn.bind('<Button-1>', lambda x: update_ko_2())
ko_2_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_2_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_2_btn.grid(row=ko_2_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_3():
    if ko_note_3_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_3_var.set("пмммо")
    elif ko_note_3_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_3_var.set("пмммомМ")
    json_in_memory["kan_otb_note_3"] = ko_note_3_var.get()
    json_in_memory["kan_otb_time_3"] = get_current_time()
    ko_3_var.set(json_in_memory["kan_otb_time_3"])
    savejson()
ko_3_label = Label(root, text='3ГР %73 К.О. / %336 %337 %339 Л.О.')
ko_3_label.grid(row=4, column=0, sticky=E, rowspan=2)
ko_3_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_3_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_3_var = StringVar()
ko_3_var.set(json_in_memory["kan_otb_time_3"])
ko_3_entry = Entry(root, textvariable=ko_3_var, state=DISABLED)
ko_3_entry.grid(row=4, column=1, sticky=W+E+S+N, columnspan=1)
ko_3_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_3_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_3_var = StringVar()
ko_note_3_var.set(json_in_memory["kan_otb_note_3"])
ko_note_3_entry = Entry(root, textvariable=ko_note_3_var, state="normal")
ko_note_3_entry.grid(row=5, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_3_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_3_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_3_btn_r = 4
ko_3_btn = Button(root, height = 1, text = 'Update')
ko_3_btn.bind('<Button-1>', lambda x: update_ko_3())
ko_3_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_3_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_3_btn.grid(row=ko_3_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_4():
    if ko_note_4_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_4_var.set("пмммо")
    elif ko_note_4_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_4_var.set("пмммомМ")
    json_in_memory["kan_otb_note_4"] = ko_note_4_var.get()
    json_in_memory["kan_otb_time_4"] = get_current_time()
    ko_4_var.set(json_in_memory["kan_otb_time_4"])
    savejson()
ko_4_label = Label(root, text='4ГР %125 К.О. / %321 %322 Л.О.')
ko_4_label.grid(row=6, column=0, sticky=E, rowspan=2)
ko_4_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_4_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_4_var = StringVar()
ko_4_var.set(json_in_memory["kan_otb_time_4"])
ko_4_entry = Entry(root, textvariable=ko_4_var, state=DISABLED)
ko_4_entry.grid(row=6, column=1, sticky=W+E+S+N, columnspan=1)
ko_4_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_4_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_4_var = StringVar()
ko_note_4_var.set(json_in_memory["kan_otb_note_4"])
ko_note_4_entry = Entry(root, textvariable=ko_note_4_var, state="normal")
ko_note_4_entry.grid(row=7, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_4_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_4_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_4_btn_r = 6
ko_4_btn = Button(root, height = 1, text = 'Update')
ko_4_btn.bind('<Button-1>', lambda x: update_ko_4())
ko_4_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_4_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_4_btn.grid(row=ko_4_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_5():
    if ko_note_5_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_5_var.set("пмммо")
    elif ko_note_5_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_5_var.set("пмммомМ")
    json_in_memory["kan_otb_note_5"] = ko_note_5_var.get()
    json_in_memory["kan_otb_time_5"] = get_current_time()
    ko_5_var.set(json_in_memory["kan_otb_time_5"])
    savejson()
ko_5_label = Label(root, text='5ГР %159 К.О. / %335 %334 Л.О.')
ko_5_label.grid(row=8, column=0, sticky=E, rowspan=2)
ko_5_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_5_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_5_var = StringVar()
ko_5_var.set(json_in_memory["kan_otb_time_5"])
ko_5_entry = Entry(root, textvariable=ko_5_var, state=DISABLED)
ko_5_entry.grid(row=8, column=1, sticky=W+E+S+N, columnspan=1)
ko_5_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_5_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_5_var = StringVar()
ko_note_5_var.set(json_in_memory["kan_otb_note_5"])
ko_note_5_entry = Entry(root, textvariable=ko_note_5_var, state="normal")
ko_note_5_entry.grid(row=9, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_5_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_5_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_5_btn_r = 8
ko_5_btn = Button(root, height = 1, text = 'Update')
ko_5_btn.bind('<Button-1>', lambda x: update_ko_5())
ko_5_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_5_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_5_btn.grid(row=ko_5_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_10():
    if ko_note_10_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_10_var.set("пмммо")
    elif ko_note_10_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_10_var.set("пмммомМ")
    json_in_memory["kan_otb_note_10"] = ko_note_10_var.get()
    json_in_memory["kan_otb_time_10"] = get_current_time()
    ko_10_var.set(json_in_memory["kan_otb_time_10"])
    savejson()
ko_10_label = Label(root, text='10ГР %121 К.О. / %330 %331 Л.О.')
ko_10_label.grid(row=10, column=0, sticky=E, rowspan=2)
ko_10_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_10_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_10_var = StringVar()
ko_10_var.set(json_in_memory["kan_otb_time_10"])
ko_10_entry = Entry(root, textvariable=ko_10_var, state=DISABLED)
ko_10_entry.grid(row=10, column=1, sticky=W+E+S+N, columnspan=1)
ko_10_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_10_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_10_var = StringVar()
ko_note_10_var.set(json_in_memory["kan_otb_note_10"])
ko_note_10_entry = Entry(root, textvariable=ko_note_10_var, state="normal")
ko_note_10_entry.grid(row=11, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_10_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_10_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_10_btn_r = 10
ko_10_btn = Button(root, height = 1, text = 'Update')
ko_10_btn.bind('<Button-1>', lambda x: update_ko_10())
ko_10_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_10_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_10_btn.grid(row=ko_10_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)

def update_ko_fp():
    if ko_note_fp_var.get() in ["п12мм12мо12", "п1212мм1212мо1212", "п2мм2мо2", "п22мм22мо22"]:
        ko_note_fp_var.set("пмммо")
    elif ko_note_fp_var.get() in ["п12мм12мо12мМ", "п2мм2мо2мМ", "п12мм12мо12мМ12", "п2мм2мо2мМ2", ]:
        ko_note_fp_var.set("пмммомМ")
    json_in_memory["kan_otb_note_fp"] = ko_note_fp_var.get()
    json_in_memory["kan_otb_time_fp"] = get_current_time()
    ko_fp_var.set(json_in_memory["kan_otb_time_fp"])
    savejson()
ko_fp_label = Label(root, text='fpГР %143 %154 К.О. / %332 %333 Л.О.')
ko_fp_label.grid(row=12, column=0, sticky=E, rowspan=2)
ko_fp_label.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_fp_label.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_fp_var = StringVar()
ko_fp_var.set(json_in_memory["kan_otb_time_fp"])
ko_fp_entry = Entry(root, textvariable=ko_fp_var, state=DISABLED)
ko_fp_entry.grid(row=12, column=1, sticky=W+E+S+N, columnspan=1)
ko_fp_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_fp_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_note_fp_var = StringVar()
ko_note_fp_var.set(json_in_memory["kan_otb_note_fp"])
ko_note_fp_entry = Entry(root, textvariable=ko_note_fp_var, state="normal")
ko_note_fp_entry.grid(row=13, column=1, sticky=W+E+S+N, columnspan=1)
ko_note_fp_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_note_fp_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_fp_btn_r = 12
ko_fp_btn = Button(root, height = 1, text = 'Update')
ko_fp_btn.bind('<Button-1>', lambda x: update_ko_fp())
ko_fp_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
ko_fp_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
ko_fp_btn.grid(row=ko_fp_btn_r, column=2, sticky=W+E+S+N, rowspan=2, columnspan=1)
last_lo_label = Label(root, text='Последнее время подтверждённх ЛО:')
last_lo_label.grid(row=14, column=0, sticky=E, rowspan=1)
last_lo_label.bind('<Enter>', lambda x: check_buttons_and_colors())
last_lo_label.bind('<Leave>', lambda x: check_buttons_and_colors())
last_lo_var = StringVar()
last_lo_var.set(json_in_memory['last_lo'])
last_lo_entry = Entry(root, textvariable=last_lo_var, state="normal")
last_lo_entry.grid(row=14, column=1, sticky=W+E+S+N, columnspan=1)
last_lo_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
last_lo_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
last_lo_btn_r = 14
last_lo_btn = Button(root, height = 1, text = '+Day')
last_lo_btn.bind('<Button-1>', lambda x: inc_day('last_lo'))
last_lo_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
last_lo_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
last_lo_btn.grid(row=last_lo_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)
last_batch_label = Label(root, text='Последнее время отгруженных рейсов:')
last_batch_label.grid(row=15, column=0, sticky=E, rowspan=1)
last_batch_label.bind('<Enter>', lambda x: check_buttons_and_colors())
last_batch_label.bind('<Leave>', lambda x: check_buttons_and_colors())
last_batch_var = StringVar()
last_batch_var.set(json_in_memory['last_batch'])
last_batch_entry = Entry(root, textvariable=last_batch_var, state="normal")
last_batch_entry.grid(row=15, column=1, sticky=W+E+S+N, columnspan=1)
last_batch_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
last_batch_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
last_batch_btn_r = 15
last_batch_btn = Button(root, height = 1, text = '+Day')
last_batch_btn.bind('<Button-1>', lambda x: inc_day('last_batch'))
last_batch_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
last_batch_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
last_batch_btn.grid(row=last_batch_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)
last_onebyone_label = Label(root, text='Последнее время отгруженных непр. накл.:')
last_onebyone_label.grid(row=16, column=0, sticky=E, rowspan=1)
last_onebyone_label.bind('<Enter>', lambda x: check_buttons_and_colors())
last_onebyone_label.bind('<Leave>', lambda x: check_buttons_and_colors())
last_onebyone_var = StringVar()
last_onebyone_var.set(json_in_memory['last_onebyone'])
last_onebyone_entry = Entry(root, textvariable=last_onebyone_var, state="normal")
last_onebyone_entry.grid(row=16, column=1, sticky=W+E+S+N, columnspan=1)
last_onebyone_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
last_onebyone_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
last_onebyone_btn_r = 16
last_onebyone_btn = Button(root, height = 1, text = '+Day')
last_onebyone_btn.bind('<Button-1>', lambda x: inc_day('last_onebyone'))
last_onebyone_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
last_onebyone_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
last_onebyone_btn.grid(row=last_onebyone_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)

def check_colors():
    green_tk = Tkinter.color(200, 255, 200)
    yellow_tk = Tkinter.color(255, 255, 200)
    red_tk = Tkinter.color(255, 200, 200)
    if last_lo_var.get() == get_safe_time():
        last_lo_entry.configure(bg=green_tk)
    elif int(last_lo_var.get()[:2]) - int(get_safe_time()[:2]) <= -2:
        last_lo_entry.configure(bg=red_tk)
    elif int(last_lo_var.get()[:2]) - int(get_safe_time()[:2]) >= 2:
        last_lo_entry.configure(bg=red_tk)
    else:
        last_lo_entry.configure(bg=yellow_tk)
    pass
    if last_batch_var.get() == get_safe_time():
        last_batch_entry.configure(bg=green_tk)
    elif int(last_batch_var.get()[:2]) - int(get_safe_time()[:2]) <= -2:
        last_batch_entry.configure(bg=red_tk)
    elif int(last_batch_var.get()[:2]) - int(get_safe_time()[:2]) >= 2:
        last_batch_entry.configure(bg=red_tk)
    else:
        last_batch_entry.configure(bg=yellow_tk)
    pass
    if last_onebyone_var.get() == get_safe_time():
        last_onebyone_entry.configure(bg=green_tk)
    elif int(last_onebyone_var.get()[:2]) - int(get_safe_time()[:2]) <= -2:
        last_onebyone_entry.configure(bg=red_tk)
    elif int(last_onebyone_var.get()[:2]) - int(get_safe_time()[:2]) >= 2:
        last_onebyone_entry.configure(bg=red_tk)
    else:
        last_onebyone_entry.configure(bg=yellow_tk)
    pass
    if Str.get_integers(ko_1_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_1_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_1_entry.configure(bg=green_tk)
        else:
            ko_note_1_entry.configure(bg=yellow_tk)
    else:        ko_note_1_entry.configure(bg=red_tk)
    if Str.get_integers(ko_2_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_2_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_2_entry.configure(bg=green_tk)
        else:
            ko_note_2_entry.configure(bg=yellow_tk)
    else:        ko_note_2_entry.configure(bg=red_tk)
    if Str.get_integers(ko_3_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_3_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_3_entry.configure(bg=green_tk)
        else:
            ko_note_3_entry.configure(bg=yellow_tk)
    else:        ko_note_3_entry.configure(bg=red_tk)
    if Str.get_integers(ko_4_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_4_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_4_entry.configure(bg=green_tk)
        else:
            ko_note_4_entry.configure(bg=yellow_tk)
    else:        ko_note_4_entry.configure(bg=red_tk)
    if Str.get_integers(ko_5_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_5_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_5_entry.configure(bg=green_tk)
        else:
            ko_note_5_entry.configure(bg=yellow_tk)
    else:        ko_note_5_entry.configure(bg=red_tk)
    if Str.get_integers(ko_10_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_10_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_10_entry.configure(bg=green_tk)
        else:
            ko_note_10_entry.configure(bg=yellow_tk)
    else:        ko_note_10_entry.configure(bg=red_tk)
    if Str.get_integers(ko_fp_var.get())[0] == Str.get_integers(get_current_time())[0]:
        if Str.get_integers(ko_fp_var.get())[3] == Str.get_integers(get_current_time())[3]:
            ko_note_fp_entry.configure(bg=green_tk)
        else:
            ko_note_fp_entry.configure(bg=yellow_tk)
    else:        ko_note_fp_entry.configure(bg=red_tk)
def check_note_length():    note_entry.configure(width=len(note_var.get()))
def check_buttons_and_colors():
    check_colors()
    check_note_length()
    if last_lo_var.get() == get_safe_time():
        global last_lo_btn
        last_lo_btn.destroy()
        last_lo_entry.grid(columnspan=2)
    else:
        if last_lo_btn.winfo_exists() == 0:
            last_lo_btn = Button(root, height = 1, text = '+Day')
            last_lo_btn.bind('<Button-1>', lambda x: inc_day('last_lo'))
            last_lo_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
            last_lo_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
            last_lo_btn.grid(row=last_lo_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)
    if last_batch_var.get() == get_safe_time():
        global last_batch_btn
        last_batch_btn.destroy()
        last_batch_entry.grid(columnspan=2)
    else:
        if last_batch_btn.winfo_exists() == 0:
            last_batch_btn = Button(root, height = 1, text = '+Day')
            last_batch_btn.bind('<Button-1>', lambda x: inc_day('last_batch'))
            last_batch_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
            last_batch_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
            last_batch_btn.grid(row=last_batch_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)
    if last_onebyone_var.get() == get_safe_time():
        global last_onebyone_btn
        last_onebyone_btn.destroy()
        last_onebyone_entry.grid(columnspan=2)
    else:
        if last_onebyone_btn.winfo_exists() == 0:
            last_onebyone_btn = Button(root, height = 1, text = '+Day')
            last_onebyone_btn.bind('<Button-1>', lambda x: inc_day('last_onebyone'))
            last_onebyone_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
            last_onebyone_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
            last_onebyone_btn.grid(row=last_onebyone_btn_r, column=2, sticky=W+E+S+N, rowspan=1, columnspan=1)
note_label = Label(root, text='Заметка:')
note_label.grid(row=17, column=0, sticky=E, rowspan=1)
note_label.bind('<Enter>', lambda x: check_buttons_and_colors())
note_label.bind('<Leave>', lambda x: check_buttons_and_colors())
note_var = StringVar()
note_var.set(json_in_memory['note'])
note_entry = Entry(root, textvariable=note_var, state="normal")
note_entry.grid(row=17, column=1, sticky=W+E+S+N, columnspan=2)
note_entry.bind('<Enter>', lambda x: check_buttons_and_colors())
note_entry.bind('<Leave>', lambda x: check_buttons_and_colors())
save_btn_r = 18
save_btn = Button(root, height = 1, text = 'Save all! and update')
save_btn.bind('<Button-1>', lambda x: savejson())
save_btn.bind('<Enter>', lambda x: check_buttons_and_colors())
save_btn.bind('<Leave>', lambda x: check_buttons_and_colors())
save_btn.grid(row=save_btn_r, column=0, sticky=W+E+S+N, rowspan=1, columnspan=3)
json_in_memory['version'] = {'major':3, 'minor':44, 'patch':3}
savejson()
root.title("SolvoUnload 3.44.3 beta")
mainloop()
