import sys
input = sys.stdin.readline


def solve(n:int, nums: list[int]) -> int:
    sumV = sum(nums)
    rtn = 0

    for i in range(n-1):
        sumV -= nums[i]
        rtn += (sumV * nums[i])

    return rtn

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(n, nums))


main()
