import sys
import collections
input = sys.stdin.readline


def main(N: int, K: int)-> int:
    rtn = -1
    Q = collections.deque()
    Q.append((N, K))
    l = len(str(N))
    zero_check = 10**(l-1) - 1
    visited = {(N,K)}
    while Q:
        n, k = Q.popleft()
        if k == 0:
            rtn = max(rtn, n)
            continue
        
        for i in range(l):
            for j in range(i+1, l):
                x = (n // 10**i) % 10
                y = (n // 10**j) % 10
                val = n - (x * (10**i) + y * (10**j)) + (x * (10**j) + y * (10**i))
                if val > zero_check and not (val, k-1) in visited:
                    visited.add((val, k-1))
                    Q.append((val, k-1))

    return rtn


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(main(N, K))