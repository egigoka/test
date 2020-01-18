#! python3
# -*- coding: utf-8 -*-
# # # bootstrap # # #
import sys
import os
import zipfile
import csv
import datetime
import platform
if sys.version[0] != "3":
    print("Python < 3.0.0 doesn't supported!")
    sys.exit()
is64 = ""
if platform.architecture()[0] == "64bit":
    is64 = " x64"
platform.architecture
requirements = []
for root, dirs, files in os.walk("requirements"+is64):
    for file in files:
        requirements.append('"' + root + '\ '[:-1] + file+'"')

def install_requirements():
    for module in requirements:
        command = "pip install --no-dependencies " + module
        if "commands" in module:
            command = "pip install --no-dependencies --upgrade " + module
        os.system(command)


try:
    import pyodbc
except ImportError:
    install_requirements()
    import pyodbc


def download_file(url, out=None, quiet=None):
    try:  # getting wget
        import wget
    except ImportError:
        install_requirements()
        import wget
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    if quiet:
        output_file_name = wget.download(url, out=out, bar=None)
    else:
        output_file_name = wget.download(url, out=out)
    print()
    return output_file_name

try:
    from commands import *
except ImportError:
    install_requirements()
try:
    from commands import *
except ImportError:
    if os.system("git --version"):  # if get error while checking git version
        if sys.platform == "win32":  # getting git
            print("Downloading git, please, wait!")
            git_file_name = download_file("http://github.com/git-for-windows/git/releases/download/v2.17.1.windows.2/Git-2.17.1.2-32-bit.exe")
            print("Installing git, please, wait!")
            os.system(git_file_name +  r' /VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS /COMPONENTS="icons,ext\reg\shellhere,assoc,assoc_sh"')
            os.environ["PATH"] = os.environ["PATH"] + r";C:\Program Files (x86)\Git\cmd;C:\Program Files\Git\cmd"
            os.system("del " + git_file_name)
        elif sys.platform in ["linux", "linux2"]:
            os.system("sudo apt-get install git")
        elif sys.platform == "darwin":
            os.system("brew install git")
        else:
            raise NotImplementedError("OS " + sys.platform + " is not supported")
# # # end bootstrap # # #

try:
    from commands.console8 import Console
    from commands.print8 import Print
    from commands.file8 import File
    from commands.str8 import Str
    from commands.process8 import Process
    from commands.cli8 import CLI
    from commands.path8 import Path
    from commands.os8 import OS
    from commands.random8 import Random
    from commands.codegen8 import Codegen
    from commands.list8 import List
    from commands.dir8 import Dir
    from commands.gui8 import Gui
    from commands.const8 import *
    from commands.time8 import Time
    from commands.network8 import Network
except ImportError:
    install_requirements()

# config
config_with_services_names_list = "services.lst"  # list of services, splitted by spaces
grafana_port = 3001
grafana_admin_user = "admin"  # changes only before Grafana setup, delete Grafana folder to reset admin account
grafana_admin_password = "GrafanaPassword!"  # changes only before Grafana setup, delete Grafana folder to reset admin account
sleep_before_connect_to_grafana = 20
if "fast" in sys.argv:
    sleep_before_connect_to_grafana = 10
if "nosleep" in sys.argv:
    sleep_before_connect_to_grafana = 0
sql_server = "EGGG-2012"
if not Network.ping(sql_server):
    sql_server = "172.28.59.20"
sql_database = "Netwrix_Auditor_Monitoring_plan_test_DB"
sql_table = "TestTable2"
sql_driver = "ODBC Driver 11 for SQL Server"
sql_authorisation = "Windows"  # SQL not implemented yet
sql_for_grafana_port = 1433
sql_sa_user = "sa"
sql_sa_password = "W!Ktps!SQL!"
grafana_sql_datasource_name = "SQL_auto_created_py"
datasource_performance_columns = ["cpu", "mem_ws", "mem_pb", "handle", "[write(mb/s)]", "[read(mb/s)]"]
last_perfcon = datasource_performance_columns[-1]
datasource_time_column_name = "time"  # don't change, Grafana read datetime only from 'time' column :(

# option to clean Grafana
if "cleangrafana" in sys.argv:
    Process.kill("grafana-server")
    Print.colored("folder 'grafana' deleting...", "red", "on_white", end="\r")
    Dir.delete(Path.extend(Path.working(), "grafana"))
    Print.colored("folder 'grafana' deleted    ", "red", "on_white")

# get some state
folders = []
files = []
for file_or_foler in Dir.list_of_files(Path.working()):
    if os.path.isfile(file_or_foler):
        files.append(file_or_foler)
        if file_or_foler.startswith("grafana") and file_or_foler.endswith(".zip"):
            grafana_zip = file_or_foler
        elif file_or_foler.startswith("cmder") and file_or_foler.endswith(".zip"):
            cmder_zip = file_or_foler
    elif os.path.isdir(file_or_foler):
        folders.append(file_or_foler)


# read from config
services = Str.get_words(File.read(config_with_services_names_list))

# add rule in Windows Firewall to access Grafana
try:
    import subprocess
    try:
        command = 'netsh advfirewall firewall delete rule name="Open Port ' + str(grafana_port) + '" protocol=tcp localport=' + str(grafana_port) + ''
        Console.get_output(command)
    except:
        pass
    command = 'netsh advfirewall firewall add rule name="Open Port ' + str(grafana_port) + '" dir=in action=allow protocol=TCP localport=' + str(grafana_port) + ''
    Console.get_output(command)
    Print.colored("Created rule for port " + str(grafana_port) + " in Windows Firewall", "green", "on_white")
except subprocess.CalledProcessError:
    Print.colored("The requested operation (creating firewall rule) requires elevation (Run as administrator).", "red", "on_white")


# downloading Grafana
if not List.wildcard_search(files, "grafana*.zip"):
    Print.colored("Getting url to Grafana zip", "green", "on_white")
    grafana_download_html = download_file("https://grafana.com/grafana/download?platform=windows", out='grdownloawin.html')
    string_ = File.read(grafana_download_html)
    url = Str.substring(string_, '<!-- /react-text --><a href="', ".zip") + ".zip"
    Print.colored("Downloading Grafana", "green", "on_white")
    grafana_zip = download_file(url)
    if "grafana" in folders:
        folders.remove("grafana")
        Dir.delete(Path.expand(Path.current(), "grafana"))
if "grafana" not in folders:
    Print.colored("Unpacking Grafana", "green", "on_white")
    zip_object = zipfile.ZipFile(grafana_zip, 'r')
    zip_object.extractall(Path.extend(Path.working(), "grafana"))
    zip_object.close()
# end of downloading Grafana

# download Cmder_mini
if not List.wildcard_search(files, "cmder*.zip"):
    Print.colored("Getting url to Cmder_mini", "green", "on_white")
    cmder_download_html = download_file("https://github.com/cmderdev/cmder/releases/latest", out='cmrdownloawin.html')
    string_ = File.read(cmder_download_html)
    for line in Str.nl(string_):
        if 'cmder_mini.zip' in line:
            url = "https://github.com" + Str.substring(line, '<a href="', '"')
            break
            sys.exit()
    Print.colored("Downloading Cmder_mini", "green", "on_white")
    cmder_zip = download_file(url)
    if "cmder_mini" in folders:
        folders.remove("cmder_mini")
        Dir.delete(Path.extend(Path.working(), "cmder_mini"))
if "cmder_mini" not in folders:
    Print.colored("Unpacking Cmder_mini", "green", "on_white")
    zip_object = zipfile.ZipFile(cmder_zip, 'r')
    zip_object.extractall(Path.extend(Path.working(), "cmder_mini"))
    zip_object.close()

# set up Cmder
path_to_cmder_config_folder = Path.extend(Path.working(), "cmder_settings")
Dir.create(Path.extend(path_to_cmder_config_folder, "config"))
File.write(Path.extend(path_to_cmder_config_folder, "config", "user-profile.cmd"), "grafana-server.exe", mode="wb")  # write statrup script for Cmder

grafana_version = Dir.list_of_files(Path.extend(Path.working(), "grafana"))[-1]
path_to_grafana_dir = Path.extend(Path.working(), "grafana", grafana_version)
path_to_grafana_bin = Path.extend(path_to_grafana_dir, "bin")
path_to_grafana_server = Path.extend(path_to_grafana_bin, "grafana-server.exe")
path_to_dashboards_jsons_store = Path.extend(path_to_grafana_dir, "conf", "provisioning", "dashboards")
path_to_cmder = Path.extend(Path.working(), "cmder_mini", "Cmder.exe")
path_to_output_links_file = Path.extend(Path.working(), "output-links.txt")

# provisioning Grafana
# create SQL datasource
'''apiVersion: 1

datasources:
  - name: MSSQL
    type: mssql
    url: localhost:1433
    database: grafana
    user: grafana
    secureJsonData:
      password: "Password!"'''  # example from docs http://docs.grafana.org/features/datasources/mssql/
text_sql_datasource = '''apiVersion: 1

datasources:
  - name: ''' + grafana_sql_datasource_name + '''
    type: mssql
    url: ''' + sql_server + ''':''' + str(sql_for_grafana_port) + '''
    database: ''' + sql_database + '''
    user: ''' + sql_sa_user + '''
    secureJsonData:
      password: "''' + sql_sa_password + '''"
'''
path_to_sql_datasource_yaml = Path.extend(path_to_grafana_dir, "conf", "provisioning", "datasources", grafana_sql_datasource_name + ".yaml")
if not os.path.isfile(path_to_sql_datasource_yaml):
    File.create(path_to_sql_datasource_yaml)
if File.read(path_to_sql_datasource_yaml) != text_sql_datasource:
    File.write(path_to_sql_datasource_yaml, text_sql_datasource, mode="wb")
    Print.colored("Added datasource from yaml", path_to_sql_datasource_yaml, newline, text_sql_datasource, "grey", "on_white")

# Create YAML to define where stores JSONS with Dashboards
path_to_sql_dashboards_location_yaml = Path.extend(path_to_grafana_dir, "conf", "provisioning", "dashboards",  "dashboards_e.yaml")
text_sql_dashboards_location_yaml = """apiVersion: 1

providers:
- name: 'default'
  orgId: 1
  folder: ''
  type: file
  disableDeletion: false
  updateIntervalSeconds: 3 #how often Grafana will scan for changed dashboards
  options:
    path1: """ + path_to_dashboards_jsons_store
if not os.path.isfile(path_to_sql_dashboards_location_yaml):
    File.create(path_to_sql_dashboards_location_yaml)
if File.read(path_to_sql_dashboards_location_yaml) != text_sql_dashboards_location_yaml:
    File.write(path_to_sql_dashboards_location_yaml, text_sql_dashboards_location_yaml, mode="wb")
    Print.colored("Added dashboards location from yaml", path_to_sql_dashboards_location_yaml, newline, text_sql_dashboards_location_yaml, "grey", "on_white")


# start Grafana server
default_grafana_config = File.read(Path.extend(path_to_grafana_dir, "conf", "defaults.ini"))
custom_grafana_config = default_grafana_config
custom_grafana_config = custom_grafana_config.replace(";admin_user = admin", "admin_user = "+grafana_admin_user)
custom_grafana_config = custom_grafana_config.replace("admin_user = admin", "admin_user = "+grafana_admin_user)
if "grafana" not in folders:
    Print.colored("grafana config admin_user set to", grafana_admin_user, "grey", "on_white")
custom_grafana_config = custom_grafana_config.replace(";admin_password = admin", "admin_password = "+grafana_admin_password)
custom_grafana_config = custom_grafana_config.replace("admin_password = admin", "admin_password = "+grafana_admin_password)
if "grafana" not in folders:
    Print.colored("grafana config admin_password set to", grafana_admin_password, "grey", "on_white")
custom_grafana_config = custom_grafana_config.replace(";http_port = 3000", "http_port = "+str(grafana_port))
custom_grafana_config = custom_grafana_config.replace("http_port = 3000", "http_port = "+str(grafana_port))
Print.colored("grafana config http_port set to", grafana_port, "grey", "on_white")
File.write(Path.extend(path_to_grafana_dir, "conf", "custom.ini"), custom_grafana_config, mode="wb")
if "fucknocmder" not in sys.argv:
    Print.colored("Starting Cmder for grafana-server.exe", "green", "on_white")
    Process.start(path_to_cmder, "/start", path_to_grafana_bin, "/c", path_to_cmder_config_folder, new_window=True)


# (re)create dashboards
class ID:
    last = 0
    @classmethod
    def get_id(cls):
        cls.last += 1
        return str(cls.last)


for service_name in services:
    Codegen.start(Path.extend(path_to_dashboards_jsons_store, service_name+".json"))
    Codegen.add_line('''{
    "annotations": {
        "list": [
            {
                "builtIn": 1,
                "datasource": "-- Grafana --",
                "enable": true,
                "hide": true,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "type": "dashboard"
            }
        ]
    },
    "editable": true,
    "gnetId": null,
    "graphTooltip": 0,
    "id": ''' + ID.get_id() + ''',
    "links": [],
    "panels": [''')
    for counter_name in datasource_performance_columns:
        Codegen.add_line('''{
    "aliasColors": {},
    "bars": false,
    "dashLength": 10,
    "dashes": false,
    "datasource": "''' + grafana_sql_datasource_name + '''",
    "fill": 1,
    "gridPos": {
        "h": 9,
        "w": 24,
        "x": 0,
        "y": 0
    },
    "id": ''' + ID.get_id() + ''',
    "legend": {
        "alignAsTable": false,
        "avg": true,
        "current": true,
        "max": true,
        "min": true,
        "show": true,
        "total": false,
        "values": true
    },
    "lines": true,
    "linewidth": 1,
    "links": [],
    "nullPointMode": "null",
    "percentage": false,
    "pointradius": 5,
    "points": false,
    "renderer": "flot",
    "seriesOverrides": [],
    "spaceLength": 10,
    "stack": false,
    "steppedLine": false,
    "targets": [
        {
            "alias": "",
            "format": "time_series",
            "hide": false,
            "rawSql": ''' + r'''"SELECT\n  ''' + counter_name + r''', time\nFROM\n  ''' + service_name + r'''\nORDER BY\n  time",
            "refId": "A"
        }
    ],
    "thresholds": [],
    "timeFrom": null,
    "timeShift": null,
    "title": "''' + counter_name + '''",
    "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
    },
    "transparent": true,
    "type": "graph",
    "xaxis": {
        "buckets": null,
        "mode": "time",
        "name": null,
        "show": true,
        "values": []
    },
    "yaxes": [
        {
            "format": "short",
            "label": null,
            "logBase": 1,
            "max": null,
            "min": null,
            "show": true
        },
        {
            "format": "short",
            "label": null,
            "logBase": 1,
            "max": null,
            "min": null,
            "show": true
        }
    ],
    "yaxis": {
        "align": false,
        "alignLevel": null
    }
    }''')
        if counter_name != last_perfcon:
            Codegen.add_line(",")  # for not adding comma to end of list
    Codegen.add_line('''  ],
    "refresh": false,
    "schemaVersion": 16,
    "style": "dark",
    "tags": [],
    "templating": {
      "list": []
    },
    "time": {
      "from": "2018-06-01T11:31:26.693Z",
      "to": "2018-06-01T11:40:55.159Z"
    },
    "timepicker": {
        "refresh_intervals": [
            "0s",
            " 1s",
            " 5s",
            "10s",
            "30s",
            "1m",
            "5m",
            "15m",
            "30m",
            "1h",
            "2h",
            "1d"
        ],
        "time_options": [
            "5m",
            "15m",
            "1h",
            "6h",
            "12h",
            "24h",
            "2d",
            "7d",
            "30d"
        ]
    },
    "timezone": "",
    "title": "''' + service_name + '''",
    "uid": "''' + service_name + '''",
    "version": 15
}''')

# Check for ODBC drivers
Print.colored("Trying check ODBC driver", "yellow", "on_white")
try:
    con = pyodbc.connect('DRIVER={' + sql_driver + '};SERVER=' + sql_server + ';UID=' + sql_sa_user + ';PWD=' + sql_sa_password + ';DATABASE=' + sql_database + '')
    con.close()
    Print.colored("ODBC drivers are okay", "green", "on_white")
except pyodbc.InterfaceError:
    Print.debug(pyodbc.drivers())
    Print.colored("Install ODBC driver manually", "red", "on_white")
    input("Press Enter to continue...")
    if "fucknocmder" not in sys.argv:
        os.system("start .")
except pyodbc.OperationalError:
    Print.colored("Timeout connect to SQL server, skip driver check", "red", "on_white")

# download ODBC drivers
for version in ["11.0", "13.0"]:
    for architecture in ["x32", "x64"]:
        link = "https://egigoka.github.io/requirements/msodbcsql-" + version + "-" + architecture + ".msi"
        if not os.path.isfile(os.path.split(link)[1]):
            Print.colored("Downloading " + architecture + " bit ODBC driver " + version, "green", "on_white")
            odbc_driver_x32_msi = download_file(link)

# check SQL connection
try:
    connect_to_sql_string = 'DRIVER={' + sql_driver + '};SERVER=' + sql_server + ';Trusted_Connection=yes;DATABASE=' + sql_database + ''
    Print.colored('SQL settings:"' + connect_to_sql_string +  '"', "grey", "on_white")
    Print.colored("Trying connect to SQL server", "yellow", "on_white")
    con = pyodbc.connect(connect_to_sql_string)
    cur = con.cursor()
    Print.colored("Successful connection to SQL", "green", "on_white")
except pyodbc.InterfaceError as err:
    try:
        #Print.colored(err, "red", "on_white")
        Print.colored("Failed trusted connection, trying to connect as sa user", "red", "on_white")
        connect_to_sql_string = 'DRIVER={' + sql_driver + '};SERVER=' + sql_server + ';UID=' + sql_sa_user + ';PWD=' + sql_sa_password + ';DATABASE=' + sql_database + ''
        Print.colored('SQL settings:"' + connect_to_sql_string + '"', "grey", "on_white")
        Print.colored("Trying connect to SQL", "yellow", "on_white")
        con = pyodbc.connect(connect_to_sql_string)
        cur = con.cursor()
        Print.colored("Successful connection to SQL", "green", "on_white")
    except pyodbc.InterfaceError as err:
        Print.colored("Cannot connect to SQL server, skip reconnect", "red", "on_white")
except pyodbc.OperationalError:
    Print.colored("Timeout connect to SQL server, skip connection", "red", "on_white")

# SQL workaround
class Table:
    @classmethod
    def get_str_cnt(cls, table_name, print_=False):
        if print_:
            print(table_name, ":")
        # SELECT all rows from employee table
        query = 'SELECT * FROM dbo.' + table_name
        cur.execute(query)
        cnt = 0
        while True:  # Fetch all rows using a while loop
            row = cur.fetchone()
            if row:
                if print_:
                    print(row)
                cnt += 1
            else:
                break
        if print_:
            print(table_name, "rows:", cnt)
        return cnt

    @classmethod
    def write_string_to_sql(cls, table_name, *values):
        # print(table_name, values)
        # input()
        #print("Adding values", values, "to", table_name)
        output_values = ""
        for value in values[:-1]:
            output_values += str(value) + ", "
        output_values += str(values[-1])
        # print(output_values)
        query = "INSERT INTO " + table_name + " VALUES (" + output_values + ");"
        # print(query)
        # if CLI.get_y_n("copy query", answer="n"):
        #     import copypaste
        #     copypaste.copy(query)
        cur.execute(query)
        con.commit()

    @classmethod
    def clean(cls, table_name):
        query = "TRUNCATE TABLE " + table_name
        cur.execute(query)
        con.commit()

    @classmethod
    def create_for_perf_count(cls, table_name):
        Print.colored("Trying to create table", table_name, "yellow", "on_white")
        query = """CREATE TABLE [dbo].[""" + table_name + """](
               [cpu] [decimal](38, 19) NOT NULL,
               [mem_ws] [decimal](38, 19) NOT NULL,
               [mem_pb] [decimal](38, 19) NOT NULL,
               [handle] [int] NOT NULL,
               [write(mb/s)] [decimal](38, 19) NOT NULL,
               [read(mb/s)] [decimal](38, 19) NOT NULL,
               [time] [datetime] NOT NULL  -- lowercase!
        )"""
        cur.execute(query)
        con.commit()
        Print.colored("Created table", table_name, "green", "on_white")

def csv_to_sql_time(time_):  # "06/01/2018 12:59:59 AM" to "'20120618 10:34:09 AM'"
    ints = Str.get_integers(row[6], float_support=False)
    def lp2(input):
        return Str.leftpad(input, 2, 0)
    if "AM" in time_.upper():
        ampm = " AM"
    elif " PM" in time_.upper():
        ampm = " PM"
    else:
        ampm = ""
    string = lp2(ints[2]) + lp2(ints[0]) + lp2(ints[1]) + " " + lp2(ints[3]) + ":" + lp2(ints[4]) + ":" + lp2(ints[5]) + ampm
    return "'" + string + "'"

# create tables if needed
for sql_table in services:
    try:
        Table.get_str_cnt(sql_table)
        Print.colored(sql_table, "SQL table exist", "grey", "on_white")
    except pyodbc.ProgrammingError as e:
        if "Invalid object name 'dbo."+sql_table in str(e):
            Table.create_for_perf_count(sql_table)
    except NameError:
        Print.colored("No connection to SQL server, skip table check", "red", "on_white")
    try:
        if "csv" in sys.argv:
            # import from CSV in same folder
            for csv_file in List.wildcard_search(files, "*.csv"):
                if Table.get_str_cnt(sql_table) > 0:
                    if CLI.get_y_n("clean table " + sql_table +" [" + str(Table.get_str_cnt(sql_table)) + "items]"):
                        before = Table.get_str_cnt(sql_table)
                        Table.clean(sql_table)
                        Print.colored(before, ">", Table.get_str_cnt(sql_table), "items", "green", "on_white")
                if CLI.get_y_n("add random data from " + csv_file + " to table " + sql_table):
                    before = Table.get_str_cnt(sql_table)
                    file_content = Str.nl(File.read(csv_file))
                    csvreader = csv.reader(file_content)
                    #print(csvreader)
                    for row in csvreader:
                        if row != []:
                            if row[6] != "Time":
                                if Random.boolean():
                                    Table.write_string_to_sql(sql_table, row[0], row[1], row[2], row[3], row[4], row[5], csv_to_sql_time(row[6]), print_=False)
                    Print.colored(before, ">", Table.get_str_cnt(sql_table), "items", "green", "on_white")
    except NameError:
        Print.colored("No connection to SQL server, skip csv import", "red", "on_white")

if not "fucknocmder" in sys.argv:
    Time.sleep(sleep_before_connect_to_grafana)
# check Grafana connection
Print.colored("Trying connect to Grafana", "yellow", "on_white")
try:
    import urllib
except ImportError:
    install_requirements()
    import urllib
try:
    tempfile = download_file("http://localhost:"+str(grafana_port), out="connect-check.tmp", quiet=True)
    if '<grafana-app class="grafana-app">' not in File.read(tempfile):
            Print.colored("Unexpected reply from Grafana", "red", "on_white")
    Print.colored("Successful connection to Grafana", "green", "on_white")
except urllib.error.URLError:
    Print.colored("Unsucc connect to Grafana", "red", "on_white")

# save links
with open(path_to_output_links_file, mode="w") as file:
    print()
    Print.colored("Saved links to", path_to_output_links_file, newline, "green", "on_white")
    pc_fqdn = Network.get_fqdn()
    for service_name in services:
        link = "http://" + pc_fqdn+":" + str(grafana_port) + "/d/" + service_name
        Print.colored(link, "green", "on_white")
        file.write(link + newline2)


# clean temp from wget
for file in Dir.list_of_files(Path.working()):
    if file.endswith(".tmp") or file.startswith("grdownloawin") or file.startswith("cmrdownloawin"):
        File.delete(file, quiet=True)

# closing sql connect
try:
    if not "nocloseconnect" in sys.argv:
        cur.close()
        con.close()
except NameError:
    Print.colored("No connection to SQL server, skip closing connection", "red", "on_white")