import sys
import collections
input = sys.stdin.readline

def solve(N, S, roads):
    graph = collections.defaultdict(list)
    total = 0
    for a, b, c in roads:
        graph[a].append((b, c))
        graph[b].append((a, c))
        total += c

    # DFS를 사용하여 S에서 가장 먼 경로 찾기
    stack = [(S, 0)]
    visited = set()
    max_dist = 0

    while stack:
        node, dist = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        max_dist = max(max_dist, dist)
        for neighbor, length in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, dist + length))

    return 2 * total - max_dist

def main():
    # 입력값
    N, S = map(int, input().split())
    roads = []
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        roads.append((a, b, c))

    # 결과 출력
    print(solve(N, S, roads))

        
if __name__ == '__main__':
    main()