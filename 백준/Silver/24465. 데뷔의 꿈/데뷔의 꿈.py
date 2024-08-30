import sys
input = sys.stdin.readline


def main():
    date = {1:20, 2:19, 3:21, 4:20, 5:21, 6:22, 7:23, 8:23, 9:23, 10:23, 11:23, 12: 22}
    def solve(arg) -> str:
        x, y = arg
        if date[x] <= y:
            return x
        return x-1 if x != 1 else 12

    # 입력값
    aloha = { solve(map(int, input().split())) for _ in range(7)}
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]
    
    # 풀이
    result = [applicant for applicant in applicants if not solve(applicant) in aloha]
    # 출력

    if result:
        for res in sorted(result):
            print(*res)
    else:
        print('ALL FAILED')


if __name__ == "__main__":
    main()

