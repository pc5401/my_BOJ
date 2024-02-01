import sys
input = sys.stdin.readline

if __name__ == '__main__':
    res = []
    N, M = map(int, input().split())
    address_info = { key : val for key , val in [input().rstrip().split() for _ in range(N)]}
    for _ in range(M):
        res.append(address_info[input().rstrip()])

    for r in res:
        print(r)