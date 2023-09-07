import sys
input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        lst = list(map(int, input().split()))
        n = lst[0]
        if n == 0:
            break
        
        leaf = 1
        for i in range(1, 2*n*1, 2):
            spl, node = lst[i], lst[i+1]
            leaf = spl * leaf - node
        print(leaf)