import sys
input = sys.stdin.readline

def solve(N: int, S: str) -> int:
    cnt = 0

    for s in S:
        if s in 'aiueo':
            cnt += 1

    return cnt

def main():
    # 입력
    N = int(input())
    S = input().rstrip()
    
    # 풀이
    result = solve(N, S)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
