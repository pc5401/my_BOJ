import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def make_trees():
    for i in range(1, N):
        trees[input_list[i]].append(i)

def dfs(v:int):
    times = []
    for i in trees[v]:
        times.append(dfs(i))
    # 가장 오래 걸리는 직원에게 먼저 전화
    times.sort(reverse=True)
    for i in range(len(times)):
        # 그 다음으로 오래 걸리는 직원에게는 이전에 전화했던 시간이 더해진 후 전화
        times[i] += i
    if times:
        return max(times) + 1
    else:
        return 0

if __name__ == "__main__":
    N = int(input())
    input_list = list(map(int,input().split()))
    trees = defaultdict(list)
    make_trees()
    print(dfs(0))
