import sys
input = sys.stdin.readline      


def solve(n: int, k: int, cart: list[int]) -> int:
    result = 0
    cart.sort(reverse=True)
    
    for i, price in enumerate(cart):
        if i % k == k-1:
            continue
        result += price
    
    return result
     

if __name__ == "__main__":
    # 입력값
    n, k = map(int, input().split())
    cart = list(map(int, input().split()))
    
    # 풀이
    result = solve(n, k, cart)

    # 출력
    print(result)