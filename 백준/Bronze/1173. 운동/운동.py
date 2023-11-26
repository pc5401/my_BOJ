import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, m, M, T, R  = map(int, input().split())
    total, time, X = 0, 0, m

    while time < N:
        if (X+T) <= M: # 운동
            X += T
            time += 1
        else:
            X = max(m, X-R)
        
        total += 1
        if total > 1e6:
            break
    
    print(total if total < 1e6 else -1)