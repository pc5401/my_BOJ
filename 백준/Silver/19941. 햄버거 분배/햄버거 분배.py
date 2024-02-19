import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().split())
    lst = list(input().rstrip())
    eaten = [ 1 if lst[i] == 'P' else 0 for i in range(N)]
    
    res = 0

    for i in range(N):
        if lst[i] == 'P':
            for j in range(i-K, i+K+1):
                if 0 <= j < N and not eaten[j]:
                    eaten[j] = 1
                    res += 1
                    break
    print(res)