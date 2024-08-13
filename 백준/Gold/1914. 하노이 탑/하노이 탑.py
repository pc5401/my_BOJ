import sys
input = sys.stdin.readline


def solve(n: int, start: int, store: int, target: int):
    if (n == 1):
        print(f'{start} {target}')
        return
    # n-1 sub 으로 
    solve(n - 1, start, target, store)
    print(f'{start} {target}')
    solve(n - 1, store, start, target)
    


def main():
    N = int(input())
    
    if (N <= 20):
        print(2**N - 1)
        solve(N, 1, 2, 3)
    else:
        print(2**N - 1)

main()

