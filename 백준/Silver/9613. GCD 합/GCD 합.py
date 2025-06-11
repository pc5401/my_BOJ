import sys
import math
input = sys.stdin.readline

def solve(nums: list[int]) -> int:
    rtn = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            rtn += math.gcd(nums[i], nums[j])
    return rtn

def main():
    # 입력
    t = int(input().strip())
    # 풀이 & 출력
    for _ in range(t):
        data = list(map(int, input().split()))
        n, nums = data[0], data[1:]
        result = solve(nums)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
