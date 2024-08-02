import sys
input = sys.stdin.readline


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    result = 0
    X = nums.pop()
    while nums:
        Y = nums.pop()
        result += (X*Y)
        X += Y

    print(result)

main()

