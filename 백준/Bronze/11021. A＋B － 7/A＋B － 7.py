import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    ans = a + b
    print(f'Case #{tc}: {ans}')