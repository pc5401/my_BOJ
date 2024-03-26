import sys

input = sys.stdin.readline

def prime_numbers() -> list[int]:
    rtn = [1] * 10001

    for i in range(2, 10001):
        if rtn[i]:
            for j in range(i+i, 10001, i):
                rtn[j] = 0

    rtn[0], rtn[1] = 0,0
    return rtn


def goldbach(n: int, table: list[int]) -> tuple[int]:
    
    for i in range(n//2, 0, -1):
        if table[i] and table[n-i]:
            return (i, n-i)


def main():
    N = int(input())
    n_lst = [int(input()) for _ in range(N)]
    prime_num_table  = prime_numbers()

    result = []
    for n in n_lst:
        result.append(goldbach(n, prime_num_table))

    for res in result:
        print(*res)

if __name__ == "__main__":
    main()
