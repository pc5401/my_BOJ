import sys
input = sys.stdin.readline

def solve(n):
    t = int(input().strip())
    s = 1
    res = 0
    for _ in range(n - 1):
        op = input().strip()
        v = int(input().strip())
        if op == '+':
            res += s * t
            s = 1
            t = v
        elif op == '-':
            res += s * t
            s = -1
            t = v
        elif op == '*':
            t = t * v
        else:  # '/'
            t = t // v
    res += s * t
    return res

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
