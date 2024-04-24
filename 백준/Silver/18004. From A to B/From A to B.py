import sys
input = sys.stdin.readline


def solve(a: int, b: int) -> int:
    rtn = 0

    Q = [[a, 0]]
    while Q:
        num, rtn = Q.pop()
        if num == b:
            return rtn
        elif num > b and num % 2 == 0:
            Q.append([num // 2, rtn + 1])
        elif num < b:
            Q.append([b, rtn + (b - num)])
        else:
            Q.append([num+1, rtn+1])
    
    return rtn

def main():
    # 입력값
    a, b = map(int, input().split())
    a: int
    b: int
    # 풀이
    result: int = solve(a, b)
    # 출력
    print(result)


if __name__ == "__main__":
    main()