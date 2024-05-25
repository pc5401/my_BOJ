import sys
input = sys.stdin.readline


def L4(N: int, M: int) -> int:
    if N > 11 and M > 3:
        return 11 * M + 4

    return -1


def main():
    # 입력값
    result = []
    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        # 풀이
        result.append(L4(N, M))
    # 출력
    for res in result:
        print(res)
    
if __name__ == "__main__":
    main()

