import sys
input = sys.stdin.readline

def solve(nums: list[int]) -> str:
    cnt1 = nums.count(1)
    cnt2 = 3 - cnt1
    return '1' if cnt1 > cnt2 else '2'

def main():
    # 입력
    nums = list(map(int, input().split()))
    # 풀이
    result = solve(nums)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
