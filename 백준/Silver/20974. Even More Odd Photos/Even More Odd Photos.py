import sys
input = sys.stdin.readline

def solve(breeds: list[int]) -> int:
    E = sum(1 for x in breeds if x % 2 == 0)
    O = len(breeds) - E
    N = len(breeds)

    for k in range(N, 0, -1):
        even_groups = (k + 1) // 2 
        odd_groups  = k // 2

        rem_even   = max(0, even_groups - E)
        min_odds   = rem_even * 2 + odd_groups

        if min_odds <= O and (O - min_odds) % 2 == 0:
            return k

    return 1

def main():
    N = int(input())
    breeds = list(map(int, input().split()))
    print(solve(breeds))

if __name__ == "__main__":
    main()
