import sys
input = sys.stdin.readline

def get_count(t, s, arr):
    cnt = 0

    if t[0] == s[0]:
        for j in range(min(t[1], s[1]), max(t[1], s[1]) + 1):
            if arr[t[0]][j] == 1:
                cnt += 1

        return cnt

    elif t[1] == s[1]:
        for i in range(min(t[0], s[0]), max(t[0], s[0]) + 1):
            if arr[i][t[1]] == 1:
                cnt += 1

        return cnt

    for i in range(min(t[0], s[0]), max(t[0], s[0]) + 1):
        for j in range(min(t[1], s[1]), max(t[1], s[1]) + 1):
            if arr[i][j] == 1:
                cnt += 1

    return cnt


def solve(N: int, arr: list[list[int]]):
    t = [-1, -1]
    s = [-1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 성규
                s[0], s[1] = i, j
                if t[0] != -1:
                    break
            elif arr[i][j] == 5:
                t[0], t[1] = i, j
                if s[0] != -1:
                    break

    if ((t[0] - s[0]) ** 2 + (t[1] - s[1]) ** 2)**(1/2) < 5:
        return 0
    
    cnt = get_count(t, s, arr)


    if cnt >= 3:
        return 1
    return 0



def main():
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]
    print(solve(N, arr))

main()


