import sys
input = sys.stdin.readline


def largest_prime_factor(n: int) -> list[int]:
    prime_factors = [1] * (n+1)
    rtn = [1] * (n+1)

    for i in range(2, n+1):
        if prime_factors[i]:
            rtn[i] = i
            for j in range(i+i, n+1, i):
                prime_factors[j] = 0
                rtn[j] = i

    rtn[0], rtn[1] = 0, 0
    return rtn


def main():
    N = int(input())
    K = int(input())
    
    lst = largest_prime_factor(N) # 최대 소인수 리스트로 

    cnt = 0
    for i in range(1, N+1):
        if lst[i] <= K:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
