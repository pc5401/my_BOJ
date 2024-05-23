import sys
input = sys.stdin.readline


def solve(N: int, dolls: list[int]) -> int:
    dolls.sort()

    doll = dolls.pop()
    lst = [doll]
    
    while dolls:
        doll = dolls.pop()
        
        flag = 0
        for i, size in enumerate(lst):
            if doll < size:
                lst[i] = doll
                flag = 1
                break

        if not flag:
            lst.append(doll)

        lst.sort(reverse=True)

    return len(lst)


def main():
    # 입력값
    N: int = int(input())
    dolls: list[int] = list(map(int, input().split()))
    # 풀이
    result: int = solve(N, dolls)

    # 출력
    print(result)
    

if __name__ == "__main__":
    main()
