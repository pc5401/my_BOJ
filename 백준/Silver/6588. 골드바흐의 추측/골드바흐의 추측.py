import sys
input = sys.stdin.readline


def prime_number(table):
    n= len(table)
    rtn = []
    for i in range(3, n):
        if table[i]:
            rtn.append(i)
            if i*2 < n:
                for j in range(i*2, n, i): table[j] = 0
    return rtn  


def solve(n: int, prime: list, table: list):
    for p in prime:
        value = n - p
        if table[value]:
            return f'{n} = {p} + {value}'
        
    return "Goldbach's conjecture is wrong."

if __name__ == "__main__":
    # 입력 & 전처리
    table = [1 if i % 2 else 0 for i in range(1000001)]
    prime = prime_number(table)

    while True:
        n = int(input())
        if n == 0:
            break
        print(solve(n, prime, table))