import sys
input = sys.stdin.readline


def solve(n: int) -> int:
    rtn = 0
    for i in range(n+1):
        for j in range(i, n+1):
            rtn += (i+j)

    return rtn


def main():
    # 입력값
    votes = [input().rstrip() for _ in range(9)]
    
    # 풀이
    candidate = {
        'Lion' : 0,
        'Tiger' : 0
    }
    for vote in votes:
        candidate[vote] += 1
    result: int = 'Lion' if candidate['Lion'] > candidate['Tiger'] else 'Tiger'
    # 출력
    print(result)


if __name__ == "__main__":
    main()