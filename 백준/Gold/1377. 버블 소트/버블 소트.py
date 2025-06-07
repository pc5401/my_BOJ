import sys
input = sys.stdin.readline

def solve(N: int, A: list[int]) -> int:
    arr = [(val, idx) for idx, val in enumerate(A, start=1)]
    arr.sort(key=lambda x: x[0])
    max_disp = 0
    for sorted_pos, (_, orig_idx) in enumerate(arr, start=1):
        disp = orig_idx - sorted_pos
        if disp > max_disp:
            max_disp = disp
    return max_disp + 1

def main():
    # 입력
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    # 풀이
    result = solve(N, A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
