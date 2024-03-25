import sys
import re


def main():
    lst = []

    for line in sys.stdin:
        lst.append(line.rstrip())
    
    for idx, value in enumerate(lst):
        changed = re.sub('BUG', '', value)
        while True:
            temp = re.sub('BUG', '', changed)
            if changed == temp:
                break
            changed = temp

        lst[idx] = changed
    
    for res in lst:
        print(res)


if __name__ == "__main__":
    main()

