#!/usr/bin/env python3
import re

def file_extensions(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    print(lines)

    missing = []
    extensions = {}

    for line in lines:
        file = line.strip()
        if "." not in file:
            missing.append(file)
            continue
        extension = re.search(r"\.([^.]+$)",file).groups()[0]
        extensions.setdefault(extension, []).append(file)

    return (missing, extensions)

def main():
    extensions = file_extensions("src/filenames.txt")
    print(f"{len(extensions[0])} files with no extension")
    for extension in extensions[1].keys():
        print(f"{extension} {len(extensions[1])}")

if __name__ == "__main__":
    main()
