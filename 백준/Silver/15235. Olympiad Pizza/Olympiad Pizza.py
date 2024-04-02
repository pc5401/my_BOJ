import sys
import collections
input = sys.stdin.readline


def solve(n: int, needs: list[int]) -> list[int]:
    
    Q = collections.deque([(i, need) for i, need in enumerate(needs)])
    rtn = [0] * n

    t = 1
    while Q:
        num, eater = Q.popleft()
        if eater == 1:
            rtn[num] = t
        else:
            Q.append((num, eater-1))
        
        t += 1

    return rtn


def main():
    # 입력값
    N = int(input())
    needs = list(map(int, input().split()))
    # 풀이 후, 출력
    print(*solve(N, needs))


if __name__ == "__main__":
    main()
