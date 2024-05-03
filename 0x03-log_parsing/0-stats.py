#!/usr/bin/python3
import sys
import re
import signal

count = 0
pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.+?)] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
count_data = {}
file_size = 0

def print_results():
    global count, file_size, count_data
    print(f"File size: {file_size}")
    sorted_keys = sorted(count_data)
    for key in sorted_keys:
        print(f"{key}: {count_data[key]}")

    count_data = {}
    count = 0
    file_size = 0

def signal_handler(sig, frame):
    try:
        print_results()
    except Exception as e:
        pass
    raise(KeyboardInterrupt)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    result = re.match(pattern, line)
    if not result:
        continue

    file_size += int(result.group(4))
    status = str(result.group(3))

    if status not in count_data:
        count_data[status] = 0
    count_data[status] += 1
    count += 1
    if count == 10:
        print_results()
