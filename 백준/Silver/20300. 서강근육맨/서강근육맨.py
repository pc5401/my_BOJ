import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    machines = list(map(int,input().split()))
    machines.sort()
    if N % 2:
        res = machines.pop()
    else:
        res = 0
    
    for i in range(N//2):
        res = max(res, machines[i] + machines.pop())
    print(res)