import sys
import math
input = sys.stdin.readline

def solve(D: int, P: int, Q: int) -> int:
    if P > Q:
        P, Q = Q, P

    ans = ((D + Q - 1) // Q) * Q
    max_b = D // Q + 1
    if max_b > P:
        max_b = P
    for b in range(max_b + 1):
        rem = D - b * Q
        if rem > 0:
            a = (rem + P - 1) // P
        else:
            a = 0
        total = b * Q + a * P
        if total < ans:
            ans = total
    return ans

def main():
    # 입력
    D, P, Q = map(int, input().split())
    # 풀이
    result = solve(D, P, Q)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
