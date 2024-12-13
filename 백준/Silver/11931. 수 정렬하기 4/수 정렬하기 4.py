import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    # 풀이
    result = sorted(nums, reverse=True)
    
    # 출력
    for res in result:
        print(res)
