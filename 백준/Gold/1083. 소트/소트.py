import sys
input = sys.stdin.readline


def solve(N: int, S: int, Arr: list) -> list:
    
    idx = 0
    s = S
    le = len(Arr)

    while s > 0:
        max_idx = 0
        max_val = 0
        for i in range(idx, s + idx+1, 1): # 범위 내 최대값
            if i >= le:
                break

            if Arr[i] > max_val:
                max_val = Arr[i]
                max_idx = i
        if idx > le:
            break

        for i in range(max_idx, idx, -1):
            temp = Arr[i-1]
            Arr[i-1] = Arr[i]
            Arr[i] = temp
            s -= 1

        idx += 1

    return Arr

if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    Arr = list(map(int, input().split()))
    S = int(input())
    print(*solve(N, S, Arr))

