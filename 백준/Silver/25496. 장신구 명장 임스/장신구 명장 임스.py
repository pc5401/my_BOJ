import sys
input = sys.stdin.readline

def solve(P: int, N: int, A: list[int]) -> int:
    # P: 초기 피로도, N: 장신구의 개수, A: 각 장신구의 피로도
    if P >= 200:
        return 0
    A.sort()
    fatigue = P
    count = 0
    for a in A:
        if fatigue < 200:
            fatigue += a
            count += 1
        else:
            break
    return count

def main():
    # 입력
    P, N = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 풀이
    result = solve(P, N, A)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
