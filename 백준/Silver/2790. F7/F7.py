import sys
input = sys.stdin.readline


def main():
    N = int(input())
    scores = [int(input()) for _ in range(N)]
    scores.sort(reverse=True)
    
    base_line = [scores[i] + i + 1 for i in range(N)]
    maxV = max(base_line)
    for i in range(1, N):
        if scores[i] + N < maxV:
            i -= 1
            break

    print(i+1)


if __name__ == "__main__":
    main()
