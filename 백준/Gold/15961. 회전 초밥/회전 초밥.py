import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력값 세팅
    N, D, K ,C = map(int,input().split())
    sushi = [int(input()) for _ in range(N)]
    data = [0] * (D+1)
    data[C] = 1

    # 초기 세팅
    cnt = 1
    for i in range(K):
        if data[sushi[i]] == 0: # 값이 있어.
            cnt += 1
        data[sushi[i]] += 1
    res = cnt

    # 회전
    for i in range(1, N):
        prev = sushi[i-1]
        next = sushi[(K+i-1) % N]
        if prev == next: # 같은 초밥
            continue

        if data[next] == 0:
            cnt += 1
        
        if data[prev] == 1:
            cnt -= 1

        data[next] += 1
        data[prev] -= 1

        res = max(cnt, res)        

    print(res)