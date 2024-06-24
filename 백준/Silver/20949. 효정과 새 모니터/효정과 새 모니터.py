import sys
input = sys.stdin.readline

def main():
    # 입력값
    N = int(input())
    PPL = [(n+1, sum(map(lambda x : int(x)**2, input().split())) ) for n in range(N)]
    PPL.sort(key=lambda x : -x[1])
    # 풀이
    result: list[int] = [num for num, ppl in PPL]

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()