import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find(node, union_find):
    if union_find[node] != node:
        union_find[node] = find(union_find[node], union_find)
    return union_find[node]

def union(a, b, union_find):
    root_a = find(a, union_find)
    root_b = find(b, union_find)

    if root_a != root_b:
        union_find[root_a] = root_b

def solve(N: int, M: int, order_list: list[list[int]]) -> list[str]:
    rtn = []
    union_find = {i: i for i in range(N+1)}
    
    for order, a, b in order_list:
        if order == 1:  # 확인 연산
            if find(a, union_find) == find(b, union_find):
                rtn.append("YES")
            else:
                rtn.append("NO")
        else:  # 합집합 연산
            union(a, b, union_find)

    return rtn

def main():
    # 입력값
    N, M = map(int, input().split())
    order_list = [list(map(int, input().split())) for _ in range(M)]
    
    # 풀이
    result = solve(N, M, order_list)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
