import sys
input = sys.stdin.readline

def solve(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[(n - 1) // 2]

def main():
    # 입력
    n = int(input().strip())
    nums = list(map(int, input().split()))
    # 풀이
    result = solve(nums)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
