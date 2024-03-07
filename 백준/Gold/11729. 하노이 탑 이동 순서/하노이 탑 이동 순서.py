import sys
input = sys.stdin.readline


def hanoi(n: int, fro: int, to: int, via: int):
    if n == 1: 
        print(f'{fro} {to}')
        return
    hanoi(n-1, fro, via, to)
    print(f'{fro} {to}')
    hanoi(n-1, via, to, fro)


if __name__ == '__main__':
    # 입력값
    N = int(input())
    print(2**N - 1)
    if N <= 20:
        hanoi(N, 1, 3, 2)