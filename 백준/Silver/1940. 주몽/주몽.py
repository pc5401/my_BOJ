import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    lst = list(map(int, input().split()))
    visited = [0]*N
    res = 0
    for i in range(N):
        if visited[i]:
            continue
        j = N - 1
        while i < j:
            if visited[j]:
                j -= 1
                continue

            if lst[i] + lst[j] == M:
                visited[i] = 1
                visited[j] = 1
                res += 1
                break
            j -= 1
    print(res)

