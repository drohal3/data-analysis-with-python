#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    res = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if line is None:
                continue
            m = re.search(r"[drwx-]{10}\s+\d+\s+[\w._-]+\s+[\w._-]+\s+(\d+)\s+([A-Z][a-z]{2})\s+(\d{1,2})\s+(\d{1,2}):(\d{1,2})\s+(.+)\n", line)
            grouped = m.groups()
            size, month, day, hour, minute, filename = grouped
            converted = (int(size), month, int(day), int(hour), int(minute), filename)
            res.append(converted)
    return res

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
