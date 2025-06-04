import sys
input = sys.stdin.readline

def solve_array(arr: list[int]) -> int:
    N = len(arr)
    # 정렬된 S
    S = sorted(arr)
    pos = 0 
    L = 0
    for x in S:
        # arr에서 x를 찾기
        while pos < N and arr[pos] != x:
            pos += 1
        if pos == N:
            break
        L += 1
        pos += 1
    return N - L

def main():
    # 입력
    P = int(input())
    for _ in range(P):
        line = input().split()
        K = int(line[0])
        N = int(line[1])
        arr = []
        while len(arr) < N:
            arr.extend(map(int, input().split()))
        # 풀이
        moves = solve_array(arr)
        # 출력
        print(f"{K} {moves}")

if __name__ == "__main__":
    main()
