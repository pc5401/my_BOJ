import sys
input = sys.stdin.readline


def solve(num: int) -> str:
    rtn = f'Pairs for {num}:'
    if num < 3:
        return rtn

    lst = []
    i, j = 1, num-1

    while i < j:
        lst.append((i, j))
        i += 1
        j -= 1

    while lst:
        i, j = lst.pop(0)
        rtn += f' {i} {j}'
        if lst:
            rtn += ','

    return rtn


def main():
    # 입력값
    N: int = int(input())
    numbers: list[int] = [int(input()) for _ in range(N)]

    # 풀이
    result: list[str] = [solve(num) for num in range(13)]
    
    # 출력
    for num in numbers:
        print(result[num])

        
if __name__ == "__main__":
    main()

