import collections

def solve(n: int, lst: list):
    q = collections.deque([[i] for i in range(1, n+1) if lst[i] == 0])

    while q:
        arr = q.popleft()
        if len(arr) == n:
            return arr
        
        for i in range(1,n+1):
            if i in arr:
                continue
            cnt = 0
            for a in arr:
                if a > i: cnt += 1
            
            if cnt == lst[i]:
                q.append(arr+[i])


if __name__ == '__main__':
    N = int(input())
    input_lst = list(map(int,input().split()))
    lst = [0] + input_lst
    res = solve(N, lst)
    print(*res)