import sys
input = sys.stdin.readline

def solve(N: int, lst: int) -> int:
    sum_of_lst = sum(lst)
    sum_of_squares = sum(x * x for x in lst)
    
    return (sum_of_lst * sum_of_lst - sum_of_squares) // 2


if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, lst)
    
    # 출력    
    print(result)