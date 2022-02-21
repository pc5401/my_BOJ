lst = [[0 for i in range(100)] for j in range(100)]
for tc in range(4):
    j1, i1, j2, i2 = map(int, input().split())
    for i in range(i1, i2):
        for j in range(j1, j2):
            lst[i][j] += 1
            
cnt = 0
for i in range(100):
    for j in range(100):
            if lst[i][j] > 0:
                cnt += 1
            
            
print(cnt)