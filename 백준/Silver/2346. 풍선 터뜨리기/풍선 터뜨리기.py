import sys
import collections

input = sys.stdin.readline

def solve(N: int, balloons: collections.deque[int]) -> list[int]:
    rtn = []
    balloons = collections.deque(enumerate(balloons, start=1))

    while balloons:
        idx, move = balloons.popleft()
        rtn.append(idx)
        
        if not balloons:
            break
        
        if move > 0:
            move = (move - 1) % len(balloons)
        else:
            move = move % len(balloons)
        
        balloons.rotate(-move)

    return rtn

def main():
    # 입력값
    N = int(input().strip())
    balloons = collections.deque(map(int, input().split()))
    # 풀이
    result = solve(N, balloons)
    # 출력
    print(*result)
    
if __name__ == "__main__":
    main()
