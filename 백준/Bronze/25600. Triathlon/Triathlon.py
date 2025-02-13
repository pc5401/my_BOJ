import sys
input = sys.stdin.readline

def solve(data: list[str]):
    n = int(data[0])
    max_score = 0
    for i in range(1, n + 1):
        a, d, g = map(int, data[i].split())
        score = a * (d + g)
        if a == (d + g):
            score *= 2
        max_score = max(max_score, score)
    return max_score

def main():
    n = int(input().rstrip())
    data = [str(n)]
    for _ in range(n):
        data.append(input().rstrip())
    
    result = solve(data)
    print(result)

if __name__ == "__main__":
    main()
