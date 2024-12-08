import sys
input = sys.stdin.readline

def solve(n: int, lst: list[int]) -> list[int]:
    for a1 in range(1, n+1):
        used = set()
        a = [a1]
        used.add(a1)
        flag = True
        for i in range(n-1):
            a_next = lst[i] - a[-1]
            if a_next < 1 or a_next > n or a_next in used:
                flag = False
                break
            a.append(a_next)
            used.add(a_next)
        if flag:
            return a
    return []

    
def main():
    # 입력값
    N = int(input())
    lst = list(map(int, input().split()))


    # 풀이
    result = solve(N, lst)
    
    # 결과 출력
    print(*result)
        
if __name__ == '__main__':
    main()