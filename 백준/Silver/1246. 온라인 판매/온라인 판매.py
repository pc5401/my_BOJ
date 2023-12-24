import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    costs = [int(input()) for _ in range(M)]
    costs.sort(key=lambda x : -x)
    
    price, maxV = 0, 0

    for i in range(1, M+1):
        cost = costs[i-1]
        cnt = i
        for j in range(0, i-1):
            if costs[j-1] < cost*2:
                break
            cnt += 1
        
        if cnt > N:
            cnt = N
        
        if maxV < cnt * cost:
            maxV = cnt * cost
            price = cost

    
    print(price, maxV)