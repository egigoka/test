#! python3
# -*- coding: utf-8 -*-
import string
import sys
import time
import datetime
try:
    from commands import *
    from commands.id9 import ID
    id = ID()
except ImportError:
    import os
    os.system("pip install git+https://github.com/egigoka/commands")
try:
    import todoist
except ImportError:
    from commands.pip9 import Pip
    Pip.install("todoist-python")
    import todoist
try:
    import pytz
except ImportError:
    from commands.pip9 import Pip
    Pip.install("pytz")
    import pytz
try:
    import tzlocal
except ImportError:
    from commands.pip9 import Pip
    Pip.install("tzlocal")
    import tzlocal


class Arguments:
    apikey = False
    if "apikey" in sys.argv:
        apikey = True

    cleanup = False
    if "cleanup" in sys.argv:
        cleanup = True

    test = False
    if "test" in sys.argv:
        test = True

    work = False
    if "work" in sys.argv:
        work = True

    list = False
    if "list" in sys.argv:
        list = True

    listnogreen = False
    if "listnogreen" in sys.argv:
        listnogreen = True

    name = False
    if "name" in sys.argv:
        name = True

    random = False
    if "random" in sys.argv:
        random = True

    loop = False
    if "loop" in sys.argv:
        loop = True


class State:
    debug = False
    debug_not_today = False
    showed_random_items = []
    loop_input = ""
    random_bench = Bench(prefix="<task> done in", fraction_digits=0)


class Priority:
    USUAL = 1
    HIGH = 2
    VERY_HIGH = 3
    EXTREMELY = 4


class Todoist:

    def __init__(self, api_key):
        Print.rewrite("Loading cache...")
        self.api = todoist.TodoistAPI(api_key)
        Print.rewrite("Syncing...")
        self.api.sync()
        Print.rewrite("Synced")

    def projects_all_names(self):
        names = {}
        for project in self.api.projects.all():
            names[project["name"]] = project["id"]
        return names

    def project_exists(self, name):
        all_projects = self.projects_all_names()
        if name in all_projects:
            return all_projects[name]
        return False

    def get_temp_project(self, prefix="Temp"):
        project_name = None
        cnt = 0
        while not project_name:
            cnt += 1
            temp_name = f"{prefix}_{cnt}"
            if not self.project_exists(temp_name):
                project_name = temp_name
        new_project = self.api.projects.add(project_name)
        return new_project

    def project_raw_items(self, name):
        if self.project_exists(name):
            project_data = self.api.projects.get_data(self.project_exists(name))
            try:
                items = project_data["items"]
            except KeyError:
                if project_data['error_tag'] == 'PROJECT_NOT_FOUND':
                    return []
            return items
        else:
            raise KeyError(f"Project {name} doesn't exist!")

    def project_items_names(self, name):
        raw = self.project_raw_items(name)
        items = {}
        for item in raw:
            items[item["content"]] = item["id"]
        return items

    def project_cnt_items(self, project_name):
        cnt_all_tasks = 0
        items = self.project_raw_items(project_name)
        for item in items:
            cnt_all_tasks += 1
        return cnt_all_tasks

    def cnt_all_items_in_account(self):
        cnt_all_tasks = 0
        for project_name, project_id in Dict.iterable(self.projects_all_names()):
            cnt_all_tasks += self.project_cnt_items(project_name)
        return cnt_all_tasks

    def project_cnt_incomplete_items(self, project_name):
        cnt_incomplete_tasks = 0
        items = self.project_raw_items(project_name)
        for item in items:
            if status in ["today", "overdue"]:
                cnt_incomplete_tasks += 1
        return cnt_incomplete_tasks

    def cnt_incompleted_items_in_account(self):
        cnt_incomplete_tasks = 0
        for project_name, project_id in Dict.iterable(self.projects_all_names()):
            cnt_incomplete_tasks += self.project_cnt_incomplete_items(project_name)
        return cnt_incomplete_tasks

    def project_raw_incomplete_items(self, project_name):
        items = self.project_raw_items(project_name)
        incomplete_items = []
        for item in items:
            status = self.item_status(item)
            if status in ["today", "overdue"]:
                incomplete_items.append(item)
        return incomplete_items

    def all_incomplete_items_in_account(self):
        incomplete_items = {}
        for project_name, project_id in Dict.iterable(self.projects_all_names()):
            incomplete_items[project_name] = self.project_raw_incomplete_items(project_name)
        return incomplete_items

    def create_project(self, name):
        project_id = self.project_exists(name)
        if not project_id:
            print(f"Creating project {name}")
            project = self.api.projects.add(name)
            self.api.commit()
            self.api.sync()
            project_id = self.project_exists(name)
        return project_id

    def add_item(self, name, project_name, item_order, day_order, priority=Priority.USUAL, date_string=None, due_date_utc=None, auto_create_project=False):
        project_id = self.project_exists(project_name)
        if auto_create_project:
            project_id = self.create_project(project_name)
        else:
            raise KeyError(f"Project {project_name} doesn't exist")
        if date_string and due_date_utc:
            raise KeyError(f"only date_string {date_string} or due_date_utc {due_date_utc}")
        elif date_string:
            item = self.api.items.add(name, project_id, item_order=item_order, date_string=date_string,
                                      day_order=day_order, priority=priority)
        elif due_date_utc:
            item = self.api.items.add(name, project_id, item_order=item_order, due_date_utc=due_date_utc,
                                      day_order=day_order, priority=priority)
        else:
            item = self.api.items.add(name, project_id, item_order=item_order, day_order=day_order, priority=priority)
        return item

    def date_string_today(self):
        return datetime.datetime.now().strftime("%d %b %Y")

    def todoist_time_to_datetime_datetime(self, time_string):
        try:
            datetime_object = datetime.datetime.strptime(time_string, "%a %d %b %Y %H:%M:%S +0000")
        except ValueError:
            try:
                datetime_object = datetime.datetime.strptime(time_string, "%d %b %Y %H:%M:%S +0000")
            except ValueError:
                try:
                    datetime_object = datetime.datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S")
                except ValueError:
                    datetime_object = datetime.datetime.strptime(time_string, "%Y-%m-%d")
        return datetime_object

    def item_status(self, item_obj):
        # Print.prettify(item_obj)
        try:
            if item_obj["is_archived"]:
                if State.debug:
                    print(item_obj["content"], item_obj["due"], "deleted")
                return "deleted"
        except KeyError:
            pass
        if item_obj['is_deleted']:
            if State.debug:
                print(item_obj["content"], item_obj["due"], "deleted")
            return "deleted"
        elif item_obj['checked']:
            if State.debug:
                print(item_obj["content"], item_obj["due"], "deleted")
            return "deleted"
        else:
            now = datetime.datetime.now()
            try:
            #if item_obj['due_date_utc']:
                todo_time = self.todoist_time_to_datetime_datetime(item_obj['due']['date'])
            except KeyError as e:
                Print.prettify(item_obj)
                Print.colored("try to 'pip install --upgrade todoist-python'")
                raise KeyError(e)
            except TypeError:
                #Print.prettify(item_obj)
                #print(id.get())
                if State.debug:
                    print(item_obj["content"], item_obj["due"], "no date")
                return "no date"
            local_timezone = tzlocal.get_localzone()
            utc_timezone = pytz.timezone("utc")
            end_of_today = datetime.datetime(now.year,
                                             now.month,
                                             now.day,
                                             23, 59, 59) # not used
            now = datetime.datetime.now()

            #end_of_today_aware = local_timezone.localize(now)

            #todo_time_aware = utc_timezone.localize(todo_time)
            # todo: update it to new api due item_obj["date"]["timezone"]
            # dirty hack:
            todo_time_aware = todo_time
            end_of_today_aware = end_of_today

            if end_of_today_aware > todo_time_aware:
                if State.debug:
                    print(item_obj["content"], item_obj["due"], "overdue")
                return "overdue"
            elif end_of_today_aware == todo_time_aware:
                if State.debug:
                    print(item_obj["content"], item_obj["due"], "today")
                return "today"
            elif end_of_today_aware < todo_time_aware:
                if State.debug or State.debug_not_today:
                    print(item_obj["content"], item_obj["due"], "not today")
                return "not today"



encrypted_todoist_token = [-20, -20, -50, -14, -61, -54, 2, 0, 32, 27, -51, -21, -54, -53, 4, 3, 29, -14, -51, 29, -10, -6, 1, 4, 28,
                           29, -55, -17, -59, -9, 2, 50, -13, -14, -52, -15, -56, -59, -44, 5]  # yes, that shitty

todoist_password_for_api_key = Str.input_pass("Enter password: ")
todoist_api_key = Str.decrypt(encrypted_todoist_token, todoist_password_for_api_key)

def main():
    todo = Todoist(todoist_api_key)
    if Arguments.apikey:
        print(f"API key: {todoist_api_key}")

    if Arguments.name:
        print("@"+todo.api.state["user"]["full_name"])

    # if Arguments.cleanup:
    #     if CLI.get_y_n(f'Do you really want to remove all data in account {todo.api.state["user"]["full_name"]}'):
    #         for task in todo.api.items.all():
    #             task.delete()
    #             Print.colored("    Task", task["content"], "deleted", "red")
    #         for project_id in todo.api.projects.all():
    #             project_id.delete()
    #             Print.colored("Project", project_id["name"], "deleted", "red")
    #         todo.api.commit()

    if Arguments.list:
        projects = todo.projects_all_names()
        for project_name, project_id in Dict.iterable(projects):
            items = todo.project_raw_items(project_name)
            Print(project_name, len(items), "items")
            for item in items:
                status = todo.item_status(item)
                status_colors = {"deleted":'magenta', "overdue":'red', "today":'yellow', "not today": 'green'}
                status_color = status_colors[status]
                if Arguments.listnogreen:
                    if status_color == "green":
                        continue  # skip green items
                Print.colored(" "*3, item['content'], status_color)

    # if Arguments.work:
    #     items = ['Wash the clothes - Shower room - 1 week', 'Clean out the tables - Kitchen - 2 days',
    #              'Wash dishes - Kitchen - 1 day', 'Take out the trash - Kitchen - 1 day',
    #              'Wash the stove - Kitchen - 1 day',
    #              'Vacuum/sweep - Kitchen - 1 day', 'Wash the floor - Kitchen - 3 days', 'Clean out - Balcony - 3 days',
    #              'Wash the floor - Balcony - 3 days', 'Clean up on the table - My room - 2 days',
    #              'Clean out - My room - 2 days', 'Wipe dust - My room - 1 week','Fill the bed - My room - 1 day',
    #              'Vacuum/sweep - My room - 1 day', 'Wash the floor - My room - 3 days',
    #              'Wash shower - Shower room - 1 day', 'Wash the sink - Shower room - 1 day',
    #              'Vacuum/sweep - Shower room - 1 day', 'Vacuum/sweep - Toilet - 1 day',
    #              'Wash the floor - Shower room - 3 days', 'Wash the floor - Toilet - 3 days',
    #              'Wash toilet - Toilet - 1 week', 'Wash and place shoes - Hallway - 2 days',
    #              'Vacuum/sweep - Corridor - 1 day', 'Vacuum/sweep - Hallway - 1 day','Wash the floor - Corridor - 3 days',
    #              'Wash the floor - Hallway - 3 days', 'Wash the sink - Kitchen - 3 days',
    #              'Clothes to gather - Balcony - 1 week','Wipe in the wardrobe - Wardrobe - 3 days']
    #
    #     cnt_order = 0
    #     for item in items:
    #         try:
    #             properties = item.split(" - ")
    #             name = properties[0]
    #             where = properties[1]
    #             repeat_time = properties[2]
    #         except IndexError:
    #             print(f"Wrong item:{item}")
    #             sys.exit(1)
    #
    #         cnt_order += 1
    #         item_order = day_order = cnt_order
    #
    #         todo.add_item(name, where, item_order, day_order, priority=Priority.USUAL,
    #                       date_string=f"{todo.date_string_today()} every {repeat_time}", auto_create_project=True)
    #         Print.debug(f'''todo.add_item({name}, {where}, {item_order}, {day_order}, priority={Priority.USUAL},
    #                       date_string=f"{todo.date_string_today()} every {repeat_time}", auto_create_project={True})''')
    #
    #     todo.api.commit()

    if Arguments.random:
        Print.rewrite("Chosing random item")

        cnt_incomplete_tasks = todo.cnt_incompleted_items_in_account()
        cnt_all_tasks = todo.cnt_all_items_in_account()
        incomplete_items = todo.all_incomplete_items_in_account()

        for project_name, project_items in Dict.iterable(incomplete_items.copy()):
            # skipping showed items
            cnt_skipped_items = 0
            for item in project_items:
                for showed_item in State.showed_random_items:
                    #Print.debug(f'{showed_item["project"]} == {project_name} {showed_item["project"] == project_name}')
                    if showed_item["project"] == project_name:
                        # print("True")
                        #Print.debug(f'showed_item["id"] {showed_item["id"]} item["id"] {item["id"]} {showed_item["name"]} {item["content"]}')
                        # Print.debug(f'{showed_item["id"]} == {item["id"]} {showed_item["id"] == item["id"]}')
                        if showed_item["id"] == item["id"]:
                            # Print("TRUE")
                            incomplete_items[project_name].pop(incomplete_items[project_name].index(item))
                            cnt_skipped_items += 1
                            cnt_incomplete_tasks -= 1
                            # Print.debug(f"removed item {showed_item}")
                            continue
                        # print(f"--End-- {showed_item}")
            # print(cnt_skipped_items)
            # end skipping showed items
            if not project_items:
                incomplete_items.pop(project_name)

        random_project_name, random_project_items = Random.item(incomplete_items)

        random_item = Random.item(random_project_items)

        highlight = ""
        if OS.windows:
            highlight = "on_white"

        Print.rewrite()
        Print.prettify(State.showed_random_items)

        cnt_completed_tasks = cnt_all_tasks-cnt_incomplete_tasks
        Print.colored(f"Unfinished tasks: {cnt_incomplete_tasks} of {cnt_all_tasks} total - {int((cnt_completed_tasks/cnt_all_tasks)*100)}% done", highlight, "blue")

        time_string = ""
        if random_item["due_date_utc"]:
            if not random_item["due_date_utc"].endswith("20:59:59 +0000"):
                time_string = random_item["date_string"]

        Print.colored(f"Random todo: {random_item['content']} <{random_project_name}> {time_string}", "cyan")

        Print.colored(f"State.loop_input = {State.loop_input} <{State.loop_input != 'n'}>, len(State.showed_random_items) = {len(State.showed_random_items)}", "red")

        State.showed_random_items.append({"project":random_project_name, "id":random_item["id"], "name":random_item["content"]})



        todo.api.commit()


if __name__ == '__main__':
    if Arguments.loop:
        while True:
            main()
            State.loop_input = input("Press Enter to reload...\r")
    else:
        main()
