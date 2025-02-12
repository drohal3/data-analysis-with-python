#!/usr/bin/env python3

def merge(L1, L2):
    l1_index = 0
    l2_index = 0
    merged = []

    while l1_index < len(L1) or l2_index < len(L2):
        l1_element = L1[l1_index] if l1_index < len(L1) else None
        l2_element = L2[l2_index] if l2_index < len(L2) else None

        print("l1_element:", l1_element)
        print("l2_element:", l2_element)

        if l2_element is None or (l1_element is not None and l1_element <= l2_element):
            merged.append(l1_element)
            l1_index += 1

        if l1_element is None or (l2_element is not None and l2_element <= l1_element):
            merged.append(l2_element)
            l2_index += 1

    return merged

def main():
    L1 = [1, 2, 3, 4, 5, 7, 8, 9, 50]
    L2 = [2, 4, 5, 6, 7, 8, 9, 25,50]

    print(merge(L1, L2))

if __name__ == "__main__":
    main()
