import sys
import re

input = sys.stdin.readline

def main():
    N = int(input())
    patten = input().rstrip().replace('*', '.*')
    file_names = [input().rstrip() for _ in range(N)]

    result = []

    for file_name in file_names:
        # print(re.search(f'{patten}', file_name))
        if re.fullmatch(patten, file_name):
            result.append('DA')
        else:
            result.append('NE')
    
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
