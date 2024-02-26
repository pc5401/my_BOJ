import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort()
    
    arr = [[0]*1002 for _ in range(1002)]
    
    for w, h in lst:
        for i in range(h):
            arr[i][w] = 1
    
    last_w = lst[-1][0]
    max_col = max(lst, key=lambda x : x[1])
    
    w, h = lst[0]
    
    while h < max_col[1]:
        w += 1

        if arr[h][w] == 1:
            while arr[h][w]:
                h += 1
            
        else:
            for i in range(h):
                arr[i][w] = 1
    
    w, h = lst[-1]
    
    while w > max_col[0]:
        w -= 1

        if arr[h][w] == 1:
            while arr[h][w]:
                h += 1
            
        else:
            for i in range(h):
                arr[i][w] = 1

    res = sum([sum(a) for a in arr])
    print(res)