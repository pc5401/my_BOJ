import sys
import collections
input = sys.stdin.readline

def get_sum_count(n: int, lst: list[int]) -> collections.Counter:
    # 누적합 리스트
    for i in range(1, n):
        lst[i] = lst[i] + lst[i-1]
    # 누적값 Count 생성
    rtn = collections.Counter(lst)
    for i in range(n):
        for j in range(i+1, n):
            value = lst[j] - lst[i] 
            if rtn.get(value):
                rtn[value] += 1
            else:
                rtn[value] = 1
    
    return rtn




def solve(target: int, long: collections.Counter, short: collections.Counter) -> int:
    rtn = 0
    for key in long.keys():
        val = target - key
        if short.get(val):
            rtn += long[key] * short[val]

    return rtn

def main():
    # 입력값
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    # 풀이
    A_count = get_sum_count(N, A)
    B_count = get_sum_count(M, B)
    result = solve(T, A_count if N > M else B_count, B_count if N > M else A_count)

    # 출력
    print(result)


if __name__ == "__main__":
    main()

