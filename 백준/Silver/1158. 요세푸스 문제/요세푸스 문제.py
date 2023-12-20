import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    res = []
    lst = [i for i in range(1, N+1)]

    idx = 0
    while lst:
        idx += (K - 1)
        while len(lst) <= idx:
            idx -= len(lst)
        res.append(lst.pop(idx))
    
    print("<" + ", ".join(map(str, res)) + ">")