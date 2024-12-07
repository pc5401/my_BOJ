import sys
input = sys.stdin.readline

def solve(nm: list[int], graph: list[list[int]], s: int) -> list[int]:
    n, m = nm
    friends = set()
    for a, b in graph:
        if a == s:
            friends.add(b)
        elif b == s:
            friends.add(a)

    friends_list = sorted(list(friends))
    return friends_list

if __name__ == "__main__":
    K = int(input())
    NM = []
    data = []
    S = []
    for _ in range(K):
        n, m = map(int, input().split())
        NM.append([n, m])
        g = [list(map(int, input().split())) for _ in range(m)]
        data.append(g)
        s = int(input())
        S.append(s)
    
    # 풀이
    result = [solve(NM[k], data[k], S[k]) for k in range(K)]
    
    # 출력
    for idx, res in enumerate(result, start=1):
        print(f'Data Set {idx}:')
        print(*res)
        print()
