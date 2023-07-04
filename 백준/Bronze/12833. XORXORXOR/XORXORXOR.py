import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A,B,C = map(int,input().split())
    print(A^B) if C % 2 else print(A)