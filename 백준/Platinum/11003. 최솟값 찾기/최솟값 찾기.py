import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split())
    lst = list(map(int,input().split()))
    
    dq = collections.deque() # 여기에는 인덱스를 저장!
    res = [0] * N

    for i in range(N):
        # 덱의 뒤쪽에서 현재 원소보다 큰 값을 제거
        while dq and lst[i] <= lst[dq[-1]]:
            dq.pop() # 이럼 dq 맨 앞에 있는 녀석은 최소값
        dq.append(i)

        # 구간의 길이가 L을 초과하면 앞쪽 원소 제거
        while dq and i - dq[0] >= L :
            dq.popleft()

        res[i] = lst[dq[0]] # 현재 최소값
    
    print(*res)