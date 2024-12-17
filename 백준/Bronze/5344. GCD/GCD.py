import sys
input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
    

if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = [map(int, input().split()) for _ in range(N)]

    # 풀이
    result = [gcd(a, b) for a, b in lst]
    
    # 출력
    for res in result:
        print(res)
