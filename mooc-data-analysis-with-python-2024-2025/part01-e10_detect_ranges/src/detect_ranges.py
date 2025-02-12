#!/usr/bin/env python3

def detect_ranges(L):
    sorted_L = sorted(L)
    result = []
    item = []

    for element in sorted_L:
        if len(item) == 0:
            item.append(element)
            continue
        if element == item[-1] + 1:
            item.append(element)
        else:
            result.append(item)
            item = [element]

    if len(item) > 0:
        result.append(item)

    def transform(item):
        if len(item) == 1:
            return item[0]

        return item[0], item[-1] + 1

    return list(map(transform, result))

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
