import sys
import bisect
input = sys.stdin.readline


def solve(n: int, A: list[int], query_list: list[list[int]]) -> list[int]:
    ans = []
    a = sorted(A)

    for query, x, *y in query_list:

        if query == 1:
            i = bisect.bisect_left(a, x)
            ans.append(n-i)
        elif query == 2:
            i = bisect.bisect_right(a, x)
            ans.append(n-i)
        else:
            i = bisect.bisect_left(a, x)
            j = bisect.bisect_right(a, *y)
            ans.append(j-i)

    return ans

def main():
    # 입력
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    query_lst = [map(int, input().split()) for _ in range(m)]

    # 풀이
    result = solve(n, A, query_lst)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()