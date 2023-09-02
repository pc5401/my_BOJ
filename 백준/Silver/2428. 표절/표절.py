import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값 초기값 계산
    N = int(input())
    solutions = sorted(list(map(int, input().split())))
    cnt = 0
    j = 0
    for i in range(N):
        while j < N and solutions[j] <= solutions[i] / 0.9:
            j += 1
        cnt += j - i - 1

    print(cnt)