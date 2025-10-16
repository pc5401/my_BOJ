import sys

input = sys.stdin.readline

def transitive_closure_bitset(n, edges):
    reach = [0] * n
    for a, b in edges:
        reach[a - 1] |= 1 << (b - 1)

    for k in range(n):
        mk = reach[k]
        bit_k = 1 << k
        for i in range(n):
            if reach[i] & bit_k:
                reach[i] |= mk
    return reach

def solve(n, edges, queries):
    reach = transitive_closure_bitset(n, edges)
    res = []
    for a, b in queries:
        a -= 1
        b -= 1
        if (reach[a] >> b) & 1:
            res.append("-1")
        elif (reach[b] >> a) & 1:
            res.append("1")
        else:
            res.append("0")
    return "\n".join(res)

def main():
    n, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(k)]
    s = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(s)]
    print(solve(n, edges, queries))

if __name__ == "__main__":
    main()
