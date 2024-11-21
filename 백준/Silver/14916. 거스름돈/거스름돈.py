import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    five = n // 5
    left = n - (five * 5)
    
    two = left // 2
    left -= two * 2

    if left == 1 and five > 0:
        return (five + two) + 2
    elif left == 1:
        return -1
    
    return five + two


if __name__ == "__main__":
    # 입력값
    n = int(input())
    # 풀이
    result = solve(n)

    # 출력
    print(result)