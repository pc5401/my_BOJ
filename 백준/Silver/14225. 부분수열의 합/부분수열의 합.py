import sys
input = sys.stdin.readline

def solve(N: int, lst: list[int]) -> int:
    lst.sort()
    i = 1

    for num in lst:
        if num <= i:
            i += num
        else:
            break
    
    return i



if __name__ == '__main__':
    # 입력값
    N = int(input())
    lst = list(map(int, input().split()))

    # 풀이
    result = solve(N, lst)

    # 출력
    print(result)