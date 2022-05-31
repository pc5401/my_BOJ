def fact(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i

    return ans



T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    res = fact(m)/(fact(m-n)*fact(n))
    print(int(res))