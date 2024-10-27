import sys
input = sys.stdin.readline


def solve(N: int) -> list[int]:
    btn_press_res = []
    
    Q = []
    addh = N // 60
    Q.append([N-addh*60, 1, [addh, 0, 0, 0, 0]])
    Q.append([N-(addh+1)*60, 1, [addh+1, 0, 0, 0, 0]])

    while Q:
        n, ten, lst = Q.pop()

        if n == 0:
            btn_press_res.append(lst)
            continue

        if n > 0 and ten:
            cnt = n // 10
            lst[1] = cnt
            Q.append([n-cnt*10, 0, lst[:]])
            lst[1] += 1
            Q.append([n-(cnt+1)*10, 0, lst[:]])
        
        elif n < 0 and ten:
            cnt = abs(n // 10) - 1
            lst[2] = cnt
            Q.append([n+cnt*10, 0, lst[:]])
            lst[2] += 1
            Q.append([n+(cnt+1)*10, 0, lst[:]])

        elif n > 0:
            lst[3] += n
            Q.append([0, 0, lst])
        elif n < 0:
            lst[4] -= n
            Q.append([0, 0, lst])
    min_press = min([sum(res) for res in btn_press_res])
    rtn = [res for res in btn_press_res if sum(res) == min_press]
    
    return sorted(rtn)[0]


if __name__ == "__main__":
    # 입력값
    T = int(input())
    lst = [int(input()) for _ in range(T)]
    # 풀이
    result = [solve(N) for N in lst]

    # 출력
    for res in result:
        print(*res)