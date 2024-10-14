import sys
input = sys.stdin.readline      


def solve(n: int) -> int:
    cnt = 0
    number = 1

    while True:

        for num in str(number):
            cnt += 1
            if cnt == n:
                return num
        
        number += 1

     

if __name__ == "__main__":
    # 입력값
    N = int(input())
    
    # 풀이
    result = solve(N)

    # 출력
    print(result)