import sys
input = sys.stdin.readline

def solve(c: int, v: int, votes: list[int]) -> tuple[int, int]:
    prefer = { i:0 for i in range(1, c+1)}

    for vote in votes:
        prefer[vote[0]] += 1

    for i in range(1, c+1):
        if prefer[i] > v // 2:
            return (i, 1)
    
    # 2차 선거
    lst = [(item, key) for key, item in prefer.items()]
    lst.sort()

    _, fst = lst.pop()
    _, scd = lst.pop()

    fst_cnt = 0
    scd_cnt = 0

    for vote in votes:
        for v in vote:
            if v == fst:
                fst_cnt += 1
                break
            elif v == scd:
                scd_cnt += 1
                break
    
    if fst_cnt > scd_cnt:
        return (fst, 2)
    return (scd, 2)



if __name__ == "__main__":
    # 입력값
    meta = []
    data = []
    
    T = int(input())
    for _ in range(T):
        c, v = map(int, input().split())
        data.append([list(map(int, input().split())) for _ in range(v)])
        meta.append([c, v])


    # 풀이
    result = [solve(meta[t][0], meta[t][1], data[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(*res)


