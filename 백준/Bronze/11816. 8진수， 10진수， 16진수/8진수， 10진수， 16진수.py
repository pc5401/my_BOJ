import sys
input = sys.stdin.readline


def solve(X: str) -> str:
    if len(X) > 2 and X[0:2] == '0x':
        return int(X[2:], 16)
        
    elif len(X) > 1 and X[0] == '0':
        return int(X[1:], 8)
    
    return X


if __name__ == '__main__':
    # 입력값
    X = input().rstrip()

    # 풀이
    result = solve(X)

    # 출력
    print(result)

