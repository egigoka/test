import time
from ping3 import ping
from colorama import Fore, Style

# List of servers to ping
servers = ['8.8.8.8', '208.67.222.222', '1.1.1.1']

def check_servers(servers):
    for server in servers:
        try:
            response_time = ping(server, timeout=2) * 1000
            if response_time is None:
                print(Fore.RED + f"{server}: Failed" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"{server}: Success ({response_time:.2f} ms)" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"{server}: Error: {str(e)}" + Style.RESET_ALL)

while True:
    check_servers(servers)
    time.sleep(10)  # Wait for 10 seconds before the next ping
