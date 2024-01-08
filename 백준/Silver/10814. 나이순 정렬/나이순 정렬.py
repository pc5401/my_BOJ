import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = [tuple(map(lambda x: int(x) if x.isdigit() else x , input().split())) for _ in range(N)]
    res = [[] for _ in range(201)]

    for age, name in lst:
        res[age].append(name)

    for age, names in enumerate(res):
        if names:
            for name in names:
                print(age, name)