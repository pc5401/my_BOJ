import sys
input = sys.stdin.readline

def solve(triplets: list[tuple[int,int,int]]) -> list[str]:
    results = []
    for a, b, c in triplets:
        sides = sorted([a, b, c])
        if sides[2]*sides[2] == sides[0]*sides[0] + sides[1]*sides[1]:
            results.append("YES")
        else:
            results.append("NO")
    return results

def main():
    # 입력
    T = int(input().strip())
    triplets = [tuple(map(int, input().split())) for _ in range(T)]
    # 풀이
    answers = solve(triplets)
    # 출력
    for i, ans in enumerate(answers, start=1):
        print(f"Case #{i}: {ans}")

if __name__ == "__main__":
    main()
