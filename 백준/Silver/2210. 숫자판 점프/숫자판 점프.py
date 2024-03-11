
from typing import List, Set


def dfs(x: int, y: int, res_set: Set[str], arr: List[str]):    
    Q = [(arr[x][y], x, y)]

    while Q:
        word, x, y= Q.pop()
        if len(word) == 6:
            res_set.add(word)
            continue

        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < 5 and 0 <= nj < 5:
                Q.append((word + arr[ni][nj], ni, nj))


def main():
    arr = [input().split() for _ in range(5)]

    res_set = set()
    for i in range(5):
        for j in range(5):
            dfs(i, j, res_set, arr)

    print(len(res_set))


if __name__ == "__main__":
    main()