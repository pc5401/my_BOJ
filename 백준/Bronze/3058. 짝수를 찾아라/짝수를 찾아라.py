import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    result = []
    for _ in range(N):
        lst = list(map(int, input().split()))
        minV, sumV = 102, 0
        for i in lst:
            if i % 2:
                continue
            minV = min(minV, i)
            sumV += i
        
        result.append((sumV, minV))
    
    for res in result:
        print(*res)