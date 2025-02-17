import sys
input = sys.stdin.readline


def count_choco(code: int, choco: list[int]) -> str:
    n = sum(choco)

    if n == 0:
        return '07H'
    
    if code < 2:
        return f'{n}7H'
    ans = ''
    
    while n > 0:
        n, mod = divmod(n, code)
        ans += str(mod)

    return f'{ans[::-1]}7H'


def order_choco(choco: list[int]) -> str:
    if sum(choco) == 0:
        return 'NULL'

    HTCKG = 'HTCKG'
    lst = sorted([(choco[i], HTCKG[i]) for i in range(5)], key=lambda x : (-x[0], x[1]))
    
    ans = ''
    for cnt, name in lst:
        if cnt == 0:
            continue
        ans += name
    return ans



def solve(M: int, choco: list[int], eated: int) -> list[str]:
    ans = []

    for eat in eated:
        code = sum(choco) % 10
        for i in range(5):
            choco[i] -= eat[i]

        ans.append(count_choco(code, choco))
        ans.append(order_choco(choco))

    return ans


def main():
    # 입력
    choco = list(map(int, input().split()))
    M = int(input())
    eated = [list(map(int, input().split())) for _ in range(M)]

    # 풀이
    result = solve(M, choco, eated)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
