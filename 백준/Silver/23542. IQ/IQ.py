import sys
input = sys.stdin.readline

def solve(n: int, arr: list[int]) -> int:
    arr.sort()
    team_sums = []

    for i in range(n):
        team_sums.append(arr[i] + arr[2*n - 1 - i])
    
    return max(team_sums) - min(team_sums)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(result)

if __name__ == "__main__":
    main()
