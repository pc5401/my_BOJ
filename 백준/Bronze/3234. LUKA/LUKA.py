import sys
input = sys.stdin.readline

def solve(X, Y, K, route):
    result = []
    x, y = 0, 0
    # 시간 0
    if abs(x - X) <= 1 and abs(y - Y) <= 1:
        result.append("0")
    for i in range(K):
        ch = route[i]
        if ch == 'I':
            x += 1
        elif ch == 'S':
            y += 1
        elif ch == 'Z':
            x -= 1
        elif ch == 'J':
            y -= 1
        if abs(x - X) <= 1 and abs(y - Y) <= 1:
            result.append(str(i + 1))
    if not result:
        result.append("-1")
    return result

def main():
    # 입력
    X, Y = map(int, input().split())
    K = int(input().strip())
    route = input().strip()
    
    # 풀이
    result = solve(X, Y, K, route)
    
    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
