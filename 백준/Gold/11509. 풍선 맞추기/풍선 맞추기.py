import sys
from array import array
input = sys.stdin.readline

def solve(N, H):
    if N == 0:
        return 0
    mx = max(H)
    cnt = array('I', [0]) * (mx + 1)
    arrows = 0
    for h in H:
        if cnt[h]:
            cnt[h] -= 1
        else:
            arrows += 1
        cnt[h - 1] += 1
    return arrows

def main():
    # 입력
    data = list(map(int, sys.stdin.buffer.read().split()))
    N = data[0]
    H = data[1:1+N]

    # 풀이
    result = solve(N, H)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
