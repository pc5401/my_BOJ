arr = [list(input()) for _ in range(8)]

cnt = 0
v = True
for i in range(8):
    if i % 2: # 짝수라면
        v = False # 검정이 먼저
    else:
        v = True # 흰색이 먼저

    for j in range(8):
        if arr[i][j] == 'F' and v:
            cnt += 0 if j % 2 else 1

        elif arr[i][j] == 'F' and not v:
            cnt += 1 if j % 2 else 0

print(cnt)
