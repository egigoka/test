import subprocess
import time
import json
import os
from datetime import datetime
from secrets import PING_HOURS as HOURS
from commands import Print

DATA_FILE = 'ping_data.json'
PING_ADDRESSES = [
    '8.8.8.8',
    '1.1.1.1'
]
PING_INTERVAL_SECONDS = 1
PROCESS_TIMEOUT = 1
MAX_LEN_PING_DATA = HOURS * 60  # one bucket per minute

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def ping_once(address):
    if os.name == "nt":
        count = "-n"
    else:
        count = "-c"
    command = ['ping', count, '1', address]

    try:
        output = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=PROCESS_TIMEOUT
        )
        if b'0 packets received' in output.stdout \
            or b'Received = 0' in output.stdout:
            return False
        else:
            return True
    except subprocess.TimeoutExpired:
        return False

def calculate_timeout_percentage(closed_buckets, current_bucket, minutes):
    cutoff_minute = int(time.time() // 60) - minutes

    total = current_bucket['total']
    timeouts = current_bucket['timeouts']

    for bucket in closed_buckets:
        if bucket['minute'] >= cutoff_minute:
            total += bucket['total']
            timeouts += bucket['timeouts']

    if total == 0:
        return 0.0
    return (timeouts / total) * 100

def format_minutes(minutes):
    h, m = divmod(minutes, 60)
    if h and m:
        return f"{h}h {m}m"
    if h:
        return f"{h}h"
    return f"{m}m"

def get_display_windows(elapsed_minutes):
    standard = [1, 5, 60, HOURS * 60]
    windows = [w for w in standard if elapsed_minutes >= w]
    if elapsed_minutes > 0 and elapsed_minutes not in standard and elapsed_minutes < HOURS * 60:
        windows.append(elapsed_minutes)
        windows.sort()
    return windows

def main():
    ping_data = load_data()
    current_minute = int(time.time() // 60)
    current_bucket = {"minute": current_minute, "total": 0, "timeouts": 0}
    start_time = time.time()

    previous_timeouts = None
    while True:
        time.sleep(PING_INTERVAL_SECONDS)

        now_minute = int(time.time() // 60)
        if now_minute != current_minute:
            ping_data.append(current_bucket)
            while len(ping_data) > MAX_LEN_PING_DATA:
                ping_data.pop(0)
            save_data(ping_data)
            current_minute = now_minute
            current_bucket = {"minute": current_minute, "total": 0, "timeouts": 0}

        for address in PING_ADDRESSES:
            timeout_occurred = not ping_once(address)
            current_bucket['total'] += 1
            if timeout_occurred:
                current_bucket['timeouts'] += 1

        elapsed_minutes = max(1, int((time.time() - start_time) / 60))
        windows = get_display_windows(elapsed_minutes)
        rolling_parts = " ".join(
            f"{format_minutes(w)}: {calculate_timeout_percentage(ping_data, current_bucket, w):.2f}%"
            for w in windows
        )

        total_timeouts = sum(b['timeouts'] for b in ping_data) + current_bucket['timeouts']
        total_pings = sum(b['total'] for b in ping_data) + current_bucket['total']

        if previous_timeouts is None:
            previous_timeouts = total_timeouts

        color = "black" if total_timeouts == previous_timeouts else "red"
        previous_timeouts = total_timeouts

        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Print.colored(
            f"{formatted_date} "
            f"TOut: {total_timeouts}/{total_pings} "
            f"{rolling_parts}",
            color
        )

if __name__ == "__main__":
    main()
