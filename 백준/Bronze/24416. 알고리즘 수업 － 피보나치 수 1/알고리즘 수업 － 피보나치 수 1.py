def fibo(n):
    global cnt

    if n == 1 or n == 2:
        cnt += 1
        return 1
    
    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    N = int(input())
    cnt = 0
    fibo(N)
    res = N - 2
    print(cnt, res)