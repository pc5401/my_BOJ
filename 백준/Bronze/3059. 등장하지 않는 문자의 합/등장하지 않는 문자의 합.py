import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        res = 0
        S = set(input().rstrip())

        for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if a in S:
                continue
            res += ord(a)
        print(res)