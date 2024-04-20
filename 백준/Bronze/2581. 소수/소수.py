import sys
input = sys.stdin.readline


def main():
    M: int = int(input())
    N: int = int(input())

    dp = [1] * (N+1)
    dp[0], dp[1] = 0,0
    
    for i in range(2, N+1):
        if dp[i]:
            for j in range(i+i, N+1, i):
                dp[j] = 0
    
    prime_numbers = []
    for i in range(M, N+1):
        if dp[i]:
            prime_numbers.append(i)
    
    if prime_numbers:
        print(sum(prime_numbers))
        print(prime_numbers[0])
    else:
        print(-1)

if __name__ == "__main__":
    main()
