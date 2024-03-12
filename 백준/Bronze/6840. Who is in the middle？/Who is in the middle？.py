import sys
input = sys.stdin.readline


def solve(bowls):
    sorted_bowls = sorted(bowls)
    return sorted_bowls[1]

def main():
    weights = [int(input()) for _ in range(3)]
    print(solve(weights))

if __name__ == "__main__":
    main()
