#! python3
# -*- coding: utf-8 -*-
from utils import openInNewWindow, path_extend, newline, openInCurrentWindow, file_backup, substring
from codegen import start_gen, add_line, shebang, end_gen
from current_paths import *
from sys import argv


isDebug = False
#isDebug = True
iterpreter_of_codegened_script = pyw
if isDebug:
    iterpreter_of_codegened_script = py
path_of_codegened_script = path_extend(share, "scripts", "solvounload", "solvounload.bat.gui.codegened.py")
file_backup(argv[0], quiet = not isDebug)

try:
    arg1 = argv[1]
except:
    arg1 = False

if True: # code stamps

    global all_labels
    all_labels = []
    def log_label(name):
        global all_labels
        all_labels += [name]
    global all_vars
    all_vars = []
    def log_var(name):
        global all_vars
        all_vars += [name]
    global all_entries
    all_entries = []
    def log_entry(name):
        global all_entries
        all_entries += [name]
    global all_buttons
    all_buttons = {}
    def log_button(name, code):
        global all_buttons
        all_buttons[name] = code
    free_row = -1
    def get_free_row():
        global free_row
        free_row += 1
        return free_row

    init_utils = "from utils import newline, file_backup, loadjson, savejson, tkinter_color, getIntegers"

    init_current_paths = "from current_paths import *"

    init_legacy = 'from solvounload import get_safe_time, get_current_time' + newline
    init_legacy += 'from solvounload import settingsJsonFile as json_on_disk'

    init_tk = "from tkinter import *" + newline
    init_tk += "root = Tk()" + newline



    # init_groups_list = 'global groups' + newline
    init_groups_list = 'groups = [{"number": "1", "ko": "158", "lo": "329 %305 %269"},' + newline
    init_groups_list += '          {"number": "2", "ko": "156", "lo": "268 %327"},' + newline
    init_groups_list += '          {"number": "3", "ko": "73", "lo":"336 %337 %339"},' + newline
    init_groups_list += '          {"number": "4", "ko": "125", "lo":"321 %322"},' + newline
    init_groups_list += '          {"number": "5", "ko": "159", "lo": "335 %334"},' + newline
    init_groups_list += '          {"number": "10", "ko": "121", "lo":"330 %331"},' + newline
    init_groups_list += '          {"number": "fp", "ko": "143 %154", "lo": "332 %333"}, ]' + newline
    exec(init_groups_list, globals())  # import groups list from uncodegened code
    entrys = ['last_lo', 'last_batch', 'last_onebyone']

    func_load_json = newline
    func_load_json += 'def reloadJSON():' + newline
    func_load_json += '    file_backup(json_on_disk)' + newline  # backup
    func_load_json += '    global json_in_memory' + newline  # globalization
    func_load_json += '    json_in_memory = loadjson(json_on_disk)' + newline
    func_load_json += 'reloadJSON()' + newline

    func_save_json = newline
    func_save_json += 'def saveJSON():' + newline
    func_save_json += '    json_in_memory["last_lo"] = last_lo_var.get()' + newline
    func_save_json += '    json_in_memory["last_batch"] = last_batch_var.get()' + newline
    func_save_json += '    json_in_memory["last_onebyone"] = last_onebyone_var.get()' + newline
    for group in groups:
        func_save_json += ('    json_in_memory["kan_otb_time_' + group["number"] + '"] = ko_' + group["number"] + '_var.get()') + newline
        func_save_json += ('    json_in_memory["kan_otb_note_' + group["number"] + '"] = ko_note_' + group["number"] + '_var.get()') + newline
    func_save_json += '    json_in_memory["note"] = note_var.get()' + newline
    func_save_json += '    check_buttons_and_colors()' + newline
    func_save_json += '    savejson(json_on_disk, json_in_memory)' + newline

    func_inc_day = 'def inc_day(var):' + newline
    func_inc_day += '    reloadJSON()' + newline
    func_inc_day += '    new_date = json_in_memory[var][:2]' + newline
    func_inc_day += '    new_date = str(int(new_date) + 1).zfill(2)' + newline
    func_inc_day += '    if new_date == "32":' + newline
    func_inc_day += '        new_month = str(int(json_in_memory[var][3:5]) + 1).zfill(2)' + newline
    func_inc_day += '        new_date = "01." + new_month' + newline # todo for entry in entries!!!
    func_inc_day += '    json_in_memory[var] = new_date + json_in_memory[var][len(new_date):]' + newline
    func_inc_day += '''    exec(var + "_var.set('" + json_in_memory[var] + "')")''' + newline
    func_inc_day += '    saveJSON()'

    func_check_colors = newline + "def check_colors():" + newline  # todo
    func_check_colors += "    green_tk = tkinter_color(200, 255, 200)" + newline
    func_check_colors += "    yellow_tk = tkinter_color(255, 255, 200)" + newline
    func_check_colors += "    red_tk = tkinter_color(255, 200, 200)" + newline
    for entry in entrys:
        func_check_colors += "    if " + entry + "_var.get() == get_safe_time():" + newline
        func_check_colors += "        " + entry + "_entry.configure(bg=green_tk)" + newline
        func_check_colors += "    elif int(" + entry + "_var.get()[:2]) - int(get_safe_time()[:2]) <= -2:" + newline
        func_check_colors += "        " + entry + "_entry.configure(bg=red_tk)" + newline
        func_check_colors += "    elif int(" + entry + "_var.get()[:2]) - int(get_safe_time()[:2]) >= 2:" + newline
        func_check_colors += "        " + entry + "_entry.configure(bg=red_tk)" + newline
        func_check_colors += "    else:" + newline
        func_check_colors += "        " + entry + "_entry.configure(bg=yellow_tk)" + newline
        func_check_colors += "    pass" + newline
    for group in groups:
        group = group["number"]
        func_check_colors += "    if getIntegers(ko_" + group + "_var.get())[0] == getIntegers(get_current_time())[0]:" + newline  # сегодня
        func_check_colors += "        if getIntegers(ko_" + group + "_var.get())[3] == getIntegers(get_current_time())[3]:" + newline  # в этот час
        func_check_colors += "            ko_note_" + group + "_entry.configure(bg=green_tk)" + newline
        func_check_colors += "        else:" + newline
        func_check_colors += "            ko_note_" + group + "_entry.configure(bg=yellow_tk)" + newline
        func_check_colors += "    else:"
        func_check_colors += "        ko_note_" + group + "_entry.configure(bg=red_tk)" + newline

    func_check_note_length = "def check_note_length():"
    func_check_note_length += "    note_entry.configure(width=len(note_var.get()))"

    func_check_safe_time = "def check_safe_time()"
    func_check_safe_time += "    safe_time_var.set(get_safe_time())"

    def func_check_buttons_and_colors():
        func_check_buttons = newline + "def check_buttons_and_colors():" + newline
        func_check_buttons += "    check_colors()" + newline
        func_check_buttons += "    check_note_length()" + newline
        for entry in entrys:
            func_check_buttons += "    if " + entry + "_var.get() == get_safe_time():" + newline
            func_check_buttons += "        global " + entry + "_btn" + newline
            func_check_buttons += "        " + entry + "_btn.destroy()" + newline
            func_check_buttons += "        " + entry + "_entry.grid(columnspan=2)" + newline
            func_check_buttons += "    else:"  + newline
            func_check_buttons += "        if " + entry + "_btn.winfo_exists() == 0:" + newline
            func_check_buttons += "            " + substring(all_buttons[entry + "_btn"], newline).replace(newline, newline + " "*12)[:-12]
        return func_check_buttons


    def bind_code(name, lambdax = "check_buttons_and_colors()"):
        code = name + ".bind('<Enter>', lambda x: check_buttons_and_colors())" + newline
        code += name + ".bind('<Leave>', lambda x: check_buttons_and_colors())" + newline
        return code


    def label_code(name, text, row, column, rowspan=1):
        name += "_label"
        log_label(name)
        code = name + " = Label(root, text='" + text + "')" + newline
        code += name + ".grid(row=" + str(row) + ", column=" + str(column) + ", sticky=E, rowspan=" + str(rowspan) + \
                ")" + newline
        code += bind_code(name)
        return code

    def entry_code(name, var_set_from, row, column, entry_state='"normal"', columnspan=1):
        varname = name + "_var"
        log_var(varname)
        entryname = name + "_entry"
        log_entry(entryname)
        code = varname + " = StringVar()" + newline
        code += varname + ".set(" + var_set_from + ")" + newline
        code += entryname + " = Entry(root, textvariable=" + name + "_var, state=" + entry_state + ")" + newline
        code += entryname + ".grid(row=" + str(row) + ", column=" + str(column) + ", sticky=W+E+S+N, " \
                            "columnspan=" + str(columnspan) + ")" + newline
        code += bind_code(entryname)
        return code

    def button_code(name, text, lambdax, row, column, rowspan=1, columnspan=1):

        code = remember_btn_row(name, row)
        name += "_btn"
        code += name + " = Button(root, height = 1, text = '" + text + "')" + newline
        code += name + ".bind('<Button-1>', lambda x: " + lambdax + ")" + newline
        code += bind_code(name)
        code += name + ".grid(row=" + name + "_r, column=" + str(column) + ", sticky=W+E+S+N, rowspan=" + \
               str(rowspan) + ", columnspan=" + str(columnspan) + ")" + newline
        log_button(name, code)
        return code

    def safe_time_row(row):
        code = label_code("safe_time", "Безопасное время:", row, column=0)
        code += entry_code("safe_time", "get_safe_time()", row, column=1, entry_state="DISABLED", columnspan=2)
        # code += button_code("safe_time", "Update", "saveJSON()", row, column=2)
        return code

    def remember_btn_row(name, row):
        name += "_btn_r"
        code = name + " = " + str(row) + newline
        return code  # create global var like 'last_lo_btn_r', that means row to recreate button

    def universal_row(name, text, entry_var_set_from, btn_text, btn_lambdax, row, row2=None, entry_var_set_from_2=None,
                      l_b_rowspan=1, entry_state='"normal"', row2_name = None):
        code = label_code(name, text, row, column=0, rowspan=l_b_rowspan)
        code += entry_code(name, entry_var_set_from, row, column=1, entry_state=entry_state)
        if row2:
            code += entry_code(row2_name, entry_var_set_from_2, row2, column=1)
        code += button_code(name, btn_text, btn_lambdax, row, column=2, rowspan=l_b_rowspan)
        return code

    def note_row(row):
        code = label_code("note", "Заметка:", row, column=0)
        code += entry_code("note", "json_in_memory['note']", row, column=1, columnspan=2)
        # code += button_code("note", "Save", "saveJSON()", row, column=2)
        return code

    def ko_line(group, ko = None, lo = None):
        code = universal_row("ko_" + group, group + 'ГР %' + ko + ' К.О. / %' + lo + ' Л.О.',  # text
                             'json_in_memory["kan_otb_time_' + group + '"]',  # entry_var_set_from
                             "Update", "update_ko_" + group + "()", get_free_row(), row2=get_free_row(),
                             entry_var_set_from_2='json_in_memory["kan_otb_note_' + group + '"]', l_b_rowspan=2,
                             entry_state="DISABLED", row2_name="ko_note_" + group)
        return code

    def ko_update_func(group):
        code = newline + 'def update_ko_' + group + '():' + newline
        # code += '    global kan_otb_note_var_' + group + newline
        code += '    if ko_note_' + group + '_var.get() == "п12мм12мо12" or ko_note_' + group + '_var.get() == "п1212мм1212мо1212":' + newline
        code += '        ko_note_' + group + '_var.set("пмммо")' + newline
        code += '    json_in_memory["kan_otb_note_' + group + '"] = ko_note_' + group + '_var.get()' + newline
        code += '    json_in_memory["kan_otb_time_' + group + '"] = get_current_time()' + newline
        code += '    ko_' + group + '_var.set(json_in_memory["kan_otb_time_' + group + '"])' + newline
        code += '    saveJSON()' + newline
        return code

    def tkinter_title(title):
        return 'root.title("' + title + '")'

    def tkinter_icon(icon_path):
        return 'root.iconbitmap("' + icon_path + '")'

    run_mainloop = "mainloop()"


# order of code
start_gen(path_of_codegened_script)

add_line(shebang)
add_line(init_utils)
add_line(init_current_paths)
add_line(init_legacy)
add_line(init_tk)
add_line(init_groups_list)
add_line(func_load_json)
add_line(func_save_json)
add_line(func_inc_day)

for group in groups:
    add_line(ko_update_func(group["number"]))
    add_line(ko_line(group["number"], ko = group["ko"], lo = group["lo"]))

#add_line(safe_time_row(row=get_free_row()))
add_line(universal_row("last_lo", "Последнее время подтверждённх ЛО:", "json_in_memory['last_lo']", "+Day", "inc_day('last_lo')", get_free_row()))
add_line(universal_row("last_batch", "Последнее время отгруженных рейсов:", "json_in_memory['last_batch']", "+Day", "inc_day('last_batch')", get_free_row()))
add_line(universal_row("last_onebyone", "Последнее время отгруженных непр. накл.:", "json_in_memory['last_onebyone']", "+Day", "inc_day('last_onebyone')", get_free_row()))

add_line(func_check_colors)
add_line(func_check_note_length)
add_line(func_check_buttons_and_colors())


add_line(note_row(get_free_row()))

add_line(button_code(name="save", text="Save all! and update", lambdax="saveJSON()", row=get_free_row(), column=0, columnspan=3))


major_v = 3
minor_v = 42
patch_v = 2
add_line("json_in_memory['version'] = {'major':" + str(major_v) + ", 'minor':"
         + str(minor_v) + ", 'patch':" + str(patch_v) + "}" + newline + "saveJSON()")
add_line(tkinter_title("SolvoUnload " + str(major_v) + "." + str(minor_v) + "." + str(patch_v) + " beta"))
add_line(run_mainloop)
end_gen()


if isDebug:
    print('generated labels:')
    print(all_labels)
    print('generated vars:')
    print(all_vars)
    print('generated entries:')
    print(all_entries)
    print('generated buttons:')
    print(all_buttons, newline * 3)
    openInCurrentWindow(iterpreter_of_codegened_script, path_of_codegened_script)
else:
    openInNewWindow(iterpreter_of_codegened_script, path_of_codegened_script)

# todo change пмммо

# todo colorize_entrys_ko (do it smarter)

# todo http://stackoverflow.com/questions/6548837/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified а не по перемещению
