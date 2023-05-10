import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    v = (n**(1/2))*4
    print(round(v,8))