import sys
input = sys.stdin.readline
    

def main():
    # 입력값
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    table = set()
    result = []

    def solve(idx: int, stack: list[int]):
        nonlocal result, lst, N

        if len(stack) == M and not tuple(stack) in table:
            table.add(tuple(stack))
            result.append(tuple(stack))
            return
        
        for i in range(idx, N):
            stack.append(lst[i])
            solve(i+1, stack)
            stack.pop()


    # # 풀이
    solve(0, [])

    # # 출력
    for res in result:
        print(*res)


if __name__ == "__main__":
    main()


