import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    not_listen = {input().rstrip() for _ in range(N)}
    not_saw = {input().rstrip() for _ in range(M)}
    lst = list(not_listen & not_saw)
    lst.sort()

    print(len(lst))
    for name in lst:
        print(name)