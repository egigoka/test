#!python3

# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r"\term")
from commands8 import *
from cs8 import *
import vk_requests
from test11vk_test_usuless_login import *

if OS.name == "winows":
    import win_unicode_console
    win_unicode_console.enable()



class Arguments:
    print_ = False
    if "print" in sys.argv or "p" in sys.argv:
        print_ = True

    spb_house = False
    if "spb_house" in sys.argv or "spb" in sys.argv or "s" in sys.argv:
        spb_house = True

    tk_test = False
    if "tk_test" in sys.argv or "tk" in sys.argv or "t" in sys.argv:
        tk_test = True


#print(varVkUser)
#print(varVkPass)
Print.rewrite("Try to log in...")
#api = vk_requests.create_api(app_id=5569080, login=varVkUser, password=varVkPass) # todo включить авторизацию
# login by login|pass broken
api = vk_requests.create_api(app_id=5569080, service_token=varVkSeviceToken)
Print.rewrite("Succesfully logged in, trying create api")
#api_status_kim = vk_requests.create_api(app_id=5569080, login=varVkUser, password=varVkPass, scope=['offline', 'status'])#, api_version='5.00')
# fucking vk
#Print.rewrite("Succesfully created api, trying create interactive api")
#api_mine_interactive = vk_requests.create_api(interactive=True, scope=['offline', 'status'])
#Print.rewrite("Created interactive api??? Trying to set status")
#api = vk_requests.create_api() # создание сессии без логина

#api_status_kim.status.set(text='Не Ким!1один')
#Print.rewrite("Status set, trying to download posts")


timeSleep = .250 # так как программа однопоточная, то чтобы вк не банил, стоит задержка в 250 мс
whitespace = "   " # отступ



def wprint(depth):
    print(whitespace * depth, end="")

def printListReversely(input_, depth=0):
    for value in input_:
        if isinstance(value, list):
            for value_ in value:
                print(whitespace * depth + (value_))  # Напечатать только ключ, так как значение это большой (не факт) лист (факт)
                #valuePrintCmd(value_, depth=depth + 1)
                printReversely(value, depth + 1)
        elif isinstance(value, dict):
            printReversely(value, depth)
        else:
            Print.prettify(input_)
            raise TypeError("Type " + str(type(input_)), " is not supported" + str(input_))


def printReversely(input_, depth=0):
    if isinstance(input_, dict):
        for key, value in sorted(input_.items(), key=lambda x: x[0]):
            #print("key", key, "type(key)", type(key), "type(value)", type(value))
            if isinstance(value, dict):
                print (whitespace*depth + (key)) # Напечатать только ключ, так как значение это большой (не факт) словарь (факт)
                #valuePrintCmd(key, depth = depth)
                printReversely(value, depth + 1)
            elif isinstance(value, list):
                print(whitespace*depth + key)
                #valuePrintCmd(key, depth = depth+1)
                printListReversely(value, depth + 1) #обход листа
            else:
                print(whitespace*depth,end="")
                if key == "date":
                    print (key, Time.rustime(customtime=value), value)
                else:
                    print (str(key), str(value)) # Напечатать и ключ, и значение, так как это просто значение
                #valuePrintCmd(key, value, depth)
    elif isinstance(input_, list):
        for key in input_: #key is value
            printListReversely(key, depth + 1)
    else:
        Print.prettify(input_)
        raise TypeError("Type " + str(type(input_)), " is not supported" + str(input_))


def printReversely(input):
    Print.prettify(input,indent=1)


class Vk:
    last_download = datetime.datetime.now()
    @classmethod
    def download_post(Vk, groupname, post_number, posts_count=1, quiet=False):
        time_started = datetime.datetime.now()
        time_delta = Time.delta(Vk.last_download, time_started)
        print(time_delta)
        if time_delta<timeSleep:
            time.sleep(timeSleep-time_delta)
        post_dict = api.wall.get(domain=groupname, count=posts_count, offset=post_number, extended=1)
        if not quiet:
            printReversely(post_dict)
        Vk.last_download = datetime.datetime.now()  # last logic line!!!
        return post_dict

    @staticmethod
    def get_url_of_post(post_dict):
        return "https://vk.com/wall-" + str(post_dict["groups"][0]["id"]) + \
                                        "_" + str(post["items"][0]["id"])


    @staticmethod
    def get_post_property(post_dict, property):
        try:
            output = post_dict['items'][0][property]
        except KeyError:
            output = post_dict['items'][0]['copy_history'][0][property]
        return output

    @staticmethod
    def get_attachments_of_post(post_dict):
        return Vk.get_post_property(post_dict, "attachments")


    @classmethod
    def get_photos_of_post(Vk, post_dict):
        attachments = Vk.get_attachments_of_post(post_dict)
        photos = []
        for attachment in attachments:
            if attachment["type"] == "photo":
                photos.append(attachment)
        return photos


    @classmethod
    def get_text_of_post(Vk, post_dict):
        return Vk.get_post_property(post_dict, "text")

    @classmethod
    def get_date_of_post(Vk, post_dict):
        date = Vk.get_post_property(post_dict, "date")
        date = Time.timestamp_to_datetime(date)
        return date


if Arguments.print_:
    while True:
        cnt = 7773 # с какого поста начинать отображать
        print()
        print("тест ", cnt)
        print()
        postCurrent = Vk.download_post("egigokasprint", cnt, quiet=False)
        for att in postCurrent["items"]["attachments"]:
            printReversely(att)
        cnt+=1
        cnt_ = 0
        print(",,,,,,,,,,,,,,,,,,,,,,,,")
        if cnt >= postCurrent ["count"]:
            print("Ошибка! Пустой пост №" + str(postCurrent['count']) + r"!")
            break



Time1 = Time.stamp()
print("Fuck"*10000)
Time2 = Time.stamp()
print(Time.delta(Time1,Time2))
print(Time.delta(Time2,Time1))




if Arguments.spb_house:
    json_file = Path.extend(Path.working(), "vk_sbp_оютное_гнездо.json")
    try:
        jsonstring = Json.load(json_file)
    except:
        Json.save(json_file, {})
    cnt = 0
    date = datetime.datetime.now()
    while date.day>=17 and date.month>=4 and date.year==2018:
        cnt += 1
        print(CLI.stick(quiet=True), Str.leftpad(cnt,3,0))
        post = Vk.download_post("yuytnoe_gnezdishko", cnt, quiet=False)
        url = Vk.get_url_of_post(post)
        photos = Vk.get_photos_of_post(post)
        text = Vk.get_text_of_post(post)
        date = Vk.get_date_of_post(post)

        jsonstring[str(cnt)] = {}

        jsonstring[str(cnt)]["url"] = url
        jsonstring[str(cnt)]["photos"] = photos
        jsonstring[str(cnt)]["full_post"] = post
        jsonstring[str(cnt)]["text"] = text
        jsonstring[str(cnt)]["date"] = date


        Print.debug("url", url,
        #            "attachments", attachments,
        #            "photos", photos,
                    "text", text,
                    "date", Time.rustime(date)
                    )



else:
    Print.rewrite(" ")
    print("Aveliable arguments:")
    dirify(Arguments)




if Arguments.tk_test:
    import tkinter
    from PIL import ImageTk, Image

    window = tkinter.Tk()
    window.title("Join")
    #window.geometry("300x300")
    window.configure(background='grey')

    path = Path.extend(Path.home(), "Desktop", "Pictures", "1496861327127533991.jpg")

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tkinter.Label(window, image = img)

    panel.grid(row=1, column=1, columnspan=3)


    exitBtn = tkinter.Button(window, text = 'Закрыть')
    def closeWindow(ev):
        window.destroy()
    exitBtn.bind("<Button-1>", closeWindow)
    exitBtn.grid(row=2,column=1)

    exit2Btn = tkinter.Button(window, text = 'Закрыть2')
    def closeWindow2(ev):
        window.destroy()
    exit2Btn.bind("<Button-1>", closeWindow2)
    exit2Btn.grid(row=2,column=2)

    exit3Btn = tkinter.Button(window, text = 'Закрыть3')
    def closeWindow3(ev):
        window.destroy()
    exit3Btn.bind("<Button-1>", closeWindow3)
    exit3Btn.grid(row=2,column=3)

    window.mainloop()
