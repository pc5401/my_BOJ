import sys
input = sys.stdin.readline      


def solve(n: int) -> int:
    return 1

     

if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    
    # 풀이
    result = [solve(n) for n in lst]

    # 출력
    for res in result:
        print(res)