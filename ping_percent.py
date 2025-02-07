import subprocess
import time
import json
import os
from datetime import datetime

DATA_FILE = 'ping_data.json'
PING_ADDRESS = '193.111.175.220'  #  '1.1.1.1'
PING_INTERVAL_SECONDS = 1
PROCESS_TIMEOUT = 10

def load_data():
    """Load existing ping data from the JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If there's a JSON error, start fresh
            return []
    return []

def save_data(data):
    """Save current ping data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def ping_once(address):
    """
    Perform a single ping to the provided address.
    Return True if timeout occurred, False if success.
    """
    # For Linux/Mac use: ['ping', '-c', '1', address]
    # For Windows use:  ['ping', '-n', '1', address]
    command = ['ping', '-n', '1', address, ]

    try:
        output = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=PROCESS_TIMEOUT # in seconds
        )
        # If "0 packets received" is in the output, it's a timeout
        # Otherwise, success

        # print(output.stdout)
        if b'0 packets received' in output.stdout \
            or b'Received = 0' in output.stdout:
            return True  # Timeout
        else:
            return False  # Success
    except subprocess.TimeoutExpired:
        # If the ping command itself times out, treat that as a timeout
        return True

def calculate_timeout_percentage(data, minutes):
    """
    Calculate the percentage of timeouts within the last `minutes`.
    """
    now = time.time()
    cutoff = now - (minutes * 60)
    recent_records = [r for r in data if r['timestamp'] >= cutoff]
    
    if not recent_records:
        return 0.0
    
    timeouts = sum(1 for r in recent_records if r['timeout'])
    return (timeouts / len(recent_records)) * 100.0

def main():
    ping_data = load_data()

    while True:
        time.sleep(PING_INTERVAL_SECONDS)
        timeout_occurred = ping_once(PING_ADDRESS)
        record = {
            "timestamp": time.time(),
            "timeout": timeout_occurred
        }
        ping_data.append(record)
        save_data(ping_data)

        # Calculate rolling stats
        last_minute = calculate_timeout_percentage(ping_data, 1)
        last_5_minutes = calculate_timeout_percentage(ping_data, 5)
        last_hour = calculate_timeout_percentage(ping_data, 60)
        last_24_hours = calculate_timeout_percentage(ping_data, 60 * 24)

        # Calculate total lifetime stats
        total_timeouts = sum(1 for entry in ping_data if entry['timeout'])
        total_pings = len(ping_data)
        overall_percent = (total_timeouts / total_pings) * 100.0 if total_pings else 0

        # Print single-line summary
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"{formatted_date} "
            f"TOut: {total_timeouts}/{total_pings} ({overall_percent:.2f}%) "
            f"1m: {last_minute:.2f}% "
            f"5m: {last_5_minutes:.2f}% "
            f"1h: {last_hour:.2f}% "
            f"24h: {last_24_hours:.2f}%"
        )

if __name__ == "__main__":
    main()
