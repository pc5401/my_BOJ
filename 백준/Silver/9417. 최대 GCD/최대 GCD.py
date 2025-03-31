import sys, math
input = sys.stdin.readline

def solve(nums: list[int]) -> int:
    result = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            result = max(result, math.gcd(nums[i], nums[j]))
    return result

def main():
    # 입력
    T = int(input().strip())
    for _ in range(T):
        nums = list(map(int, input().split()))
        # 풀이
        result = solve(nums)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
