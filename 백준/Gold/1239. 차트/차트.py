import sys
import itertools

input = sys.stdin.readline

def solve(N, arr):
    

    best = 0
    for perm in itertools.permutations(arr):
        s = 0
        positions = {0}
        for x in perm:
            s = (s + x) % 100
            positions.add(s)

        cnt = 0
        for p in positions:
            if (p + 50) % 100 in positions:
                cnt += 1
        diam = cnt // 2

        if diam > best:
            best = diam

    return best

def main():
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))

    # 풀이
    result = solve(N, arr)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
