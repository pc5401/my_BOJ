import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값
    N = int(input())
    towers = list(map(int, input().split()))
    lasers = [(towers[-1], N-1)]
    res = [0]*N

    for i in range(N-2, -1, -1):
        if towers[i] >= towers[i+1]:
            while lasers and lasers[-1][0] <= towers[i]:
                h, num = lasers.pop()
                res[num] = i+1
        
        lasers.append((towers[i], i))
    
    print(*res)
