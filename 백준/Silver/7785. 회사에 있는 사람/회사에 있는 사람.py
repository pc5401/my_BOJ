import sys
input = sys.stdin.readline


def solve(lst: list[list[str]]) -> list[str]:
    company = set()

    for name, status in lst:
        if status == 'enter':
            company.add(name)
        else:
            company.remove(name)
    
    result = list(company)
    result.sort(reverse=True)
    
    return result


def main():
    # 입력값
    N = int(input())
    lst = [input().split() for _ in range(N)]
    
    # 풀이
    result: list[str] = solve(lst)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()