import sys
input = sys.stdin.readline


def solve(n: int) -> int:
    rtn = 0
    Q = ['1', '2']

    while Q:
        number = Q.pop()
        if len(number) == n:
            if not int(number) % 3:
                rtn += 1
            continue
        
        for added in '012':
            Q.append(number+added)
    
    return rtn


def main():
    # 입력값
    N = int(input())

    if N == 0:
        res = 0
    else:
        res = solve(N)

    print(res)

if __name__ == "__main__":
    main()
