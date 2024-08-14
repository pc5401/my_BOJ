import sys
input = sys.stdin.readline


def main():
    N = int(input())
    plus = []
    minus = []
    for _ in range(N):
        a, b = map(int, input().split())
        plus.append(a+b)
        minus.append(a-b)
    
    plus.sort()
    minus.sort()

    result = max(plus[N-1] - plus[0], minus[N-1] - minus[0])
    print(result)


main()