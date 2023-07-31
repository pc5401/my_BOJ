import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    while True:
        v = int(input())
        if v == 0:
            break

        if v % N:
            print(f'{v} is NOT a multiple of {N}.')
        else:
            print(f'{v} is a multiple of {N}.')