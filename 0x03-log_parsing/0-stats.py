#!/usr/bin/python3
""" log parsing implementation """
import sys
import re

count = 0
pattern = r'(.+?) - \[(.+?)] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
count_data = {}
file_size = 0


def print_results():
    """ print results function """
    print(f"File size: {file_size}")
    sorted_keys = sorted(count_data)
    for key in sorted_keys:
        print(f"{key}: {count_data[key]}")


try:
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
            count = 0
finally:
    print_results()
