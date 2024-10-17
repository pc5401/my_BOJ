import sys
input = sys.stdin.readline      


def solve(N: int, ABC:list[int]) -> int:
    result = 0

    for V in ABC:
        result += N if N < V else V

    return result
        

if __name__ == "__main__":
    # 입력값
    N = int(input())
    ABC = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, ABC)

    # 출력
    print(result)