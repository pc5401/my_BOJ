import sys
input = sys.stdin.readline

def counter(data: list[int]) -> str:
    cnt: dict[int, int] = dict()
    for num in data:
        if cnt.get(num):
            cnt[num] += 1
        else:
            cnt[num] = 1
    
    max_value: int = 0
    max_key: int = 0
    for key, value in cnt.items():
        if max_value < value:
            max_value = value
            max_key = key

    if max_value >= len(data) / 2 :
        return str(max_key)
    else:
        return "SYJKGW"


def solve(n: int, T: list[list[int]]) -> list[str]:
    rtn: list[str] = []
    
    for data in T:
        rtn.append(counter(data))

    return rtn


def main():
    # 입력값
    n: int = int(input())
    T: list[list[int]] = [list(map(int, input().split())) for _ in range(n)]
    # 풀이
    result = solve(n, T)
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()