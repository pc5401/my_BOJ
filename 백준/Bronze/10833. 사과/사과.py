import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    total_leftover = 0
    for _ in range(N):
        students, apples = map(int, input().split())
        leftover = apples % students
        total_leftover += leftover
    print(total_leftover)

def main():
    solve()

if __name__ == "__main__":
    main()
