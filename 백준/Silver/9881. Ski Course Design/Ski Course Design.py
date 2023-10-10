import sys
input = sys.stdin.readline


def solve(N: int, hills: list):
    hills.sort()
    rtn = float('INF')

    def how_much(minH, maxH):
        cost = 0
        for i in range(N):
            if hills[i] > maxH:
                cost += (hills[i] - maxH)**2
            elif hills[i] < minH:
                cost += (hills[i] - minH)**2
        
        return cost

    for minH in range(84):
        rtn = min(how_much(minH, minH+17), rtn)
    
    return rtn


if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    hills = [int(input()) for _ in range(N)]
    print(solve(N, hills))