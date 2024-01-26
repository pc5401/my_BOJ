import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x : (x[1], x[0]))
    
    for l in lst:
        print(*l)