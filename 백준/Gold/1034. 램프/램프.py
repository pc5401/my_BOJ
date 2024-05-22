import sys
import collections
input = sys.stdin.readline


def solve(N: int, M: int, K: int, lamp_map: list[list[int]]) -> int:
    """
    동일 패턴 그룹화 & 패턴 기반 최적화 
    """
    patterns = collections.defaultdict(int)

    for lamps in lamp_map:
        patterns[tuple(lamps)] += 1

    rtn = 0

    for pattern, cnt in patterns.items():
        zero_cnt = pattern.count(0)

        # 0의 개수가 K번 이하이고 K와 0의 개수가 모두 홀수이거나 모두 짝수일 경우
        if zero_cnt <= K and (K - zero_cnt) % 2 == 0:
            rtn = max(rtn, cnt) # 해당 패턴과 같은 행의 수를 최대 켜진 행의 수와 비교

    return rtn

def main():
    # 입력값
    N, M = map(int, input().split())
    N: int
    M: int
    lamp_map: list[list[int]] = [list(map(int, input().rstrip())) for _ in range(N)]
    K: int = int(input())

    # 풀이
    result = solve(N, M, K, lamp_map)

    # 출력
    print(result)
    
if __name__ == "__main__":
    main()

