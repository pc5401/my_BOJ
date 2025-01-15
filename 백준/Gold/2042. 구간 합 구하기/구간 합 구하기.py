import sys
import math
input = sys.stdin.readline

def make_tree(N: int, nums: list[int]):
    h = math.ceil(math.log2(N))
    tree_size = 1 << (h+1)
    rtn = [0] * tree_size

    def init(arr, tree, node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            init(arr, tree, node*2, start, (start+end) // 2)
            init(arr, tree, node*2+1, (start+end) // 2 + 1, end)
            tree[node] = tree[node*2] + tree[node*2 + 1]


    init(nums, rtn, 1, 0, N-1)

    return rtn


def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum


def solve(N: int, M: int, K: int, nums: list[int], changed: list[list[int]]) -> list[int]:
    rtn = []
    tree = make_tree(N, nums)

    for a, b, c in changed:
        if a == 1:
            update(nums, tree, 1, 0, N-1, b-1, c)
        else:
            rtn.append(query(tree, 1, 0, N-1, b-1, c-1))

    return rtn


if __name__ == '__main__':
    # 입력값
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    changed = [map(int, input().split()) for _ in range(M+K)]
    
    # 풀이
    result = solve(N, M, K, nums, changed)

    # 출력
    for res in result:
        print(res)
    