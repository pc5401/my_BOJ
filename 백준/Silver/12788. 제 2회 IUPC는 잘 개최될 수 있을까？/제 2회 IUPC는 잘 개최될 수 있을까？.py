import sys
input = sys.stdin.readline

def solve(M: int, K: int, A: list[int]) -> str:
    needed = M * K
    A.sort(reverse=True)
    total = 0
    count = 0
    for pens in A:
        if total >= needed:
            break
        total += pens
        count += 1
    if total < needed:
        return "STRESS"
    return str(count)

def main():
    # 입력
    N = int(input().strip())
    M, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 풀이
    result = solve(M, K, A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
