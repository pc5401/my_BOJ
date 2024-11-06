import sys
input = sys.stdin.readline

def solve(n1: int, n2: int) -> int:
    if n1 == n2:
        return 0
    
    elif n1 > n2:
        a = -(n1 - n2)
        b = ((360 - n1) + n2)
    
    else:
        a = n2 - n1
        b = -((360 - n2) + n1)
    
    b = 180 if b == -180 else b
    a = 180 if a == -180 else a

    if abs(a) <= abs(b):
        return a
    return b


def main():
    # 입력값
    n1 = int(input())
    n2 = int(input())
    
    # 풀이
    result = solve(n1, n2)
    
    # 출력
    print(result)

if __name__ == '__main__':
    main()
