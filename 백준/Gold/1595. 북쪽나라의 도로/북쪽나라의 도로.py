import sys

def farthest(start, adj):
    maxd = -1
    far = start
    stack = [(start, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        if d > maxd:
            maxd, far = d, u
        for v, w in adj.get(u, []):
            if v != p:
                stack.append((v, u, d + w))
    return far, maxd

def solve(edges):
    if not edges:
        return 0
    adj = {}
    nodes = set()
    for a, b, w in edges:
        nodes.add(a); nodes.add(b)
        adj.setdefault(a, []).append((b, w))
        adj.setdefault(b, []).append((a, w))
    any_node = next(iter(nodes))
    s, _ = farthest(any_node, adj)
    _, diameter = farthest(s, adj)
    return diameter

def main():
    #입력
    data = sys.stdin.read().strip().split()
    edges = []
    for i in range(0, len(data), 3):
        a = int(data[i]); b = int(data[i+1]); w = int(data[i+2])
        edges.append((a, b, w))
    #풀이
    ans = solve(edges)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
