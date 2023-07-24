import sys
import collections
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    data = list(map(int,input().split()))
    X_node = int(input())
    tree = collections.defaultdict(list)

    for i, v in enumerate(data):
        if v == -1:
            start = i

        if i == X_node:
            continue
        tree[v].append(i)

    cnt = 0
    que = collections.deque()
    que.append(start)

    while que:
        v = que.popleft()

        if v == X_node:
            continue

        if not tree[v]:
            cnt += 1
            continue

        for i in tree[v]:
            que.append(i)

    print(cnt)

# 루트 노트가 0 이 아닐 경우 -> 해결
# 루트만 남는 경우 -> 해결
