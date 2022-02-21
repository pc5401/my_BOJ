# 입력 처리
sero, garo = map(int, input().split())

sero_idx = []
garo_idx = []

n = int(input())
for _ in range(n):
    line, idx = map(int, input().split())
    # 세로
    if line == 1:
        sero_idx.append(idx)
    else:
        garo_idx.append(idx)

# 정렬
sero_idx.append(sero)
sero_idx.sort()
garo_idx.append(garo)
garo_idx.sort()

# 세로 최대값
sero_max = 0
forth = 0
for j in sero_idx:
    back = j - forth
    if back > sero_max:
        sero_max = back
    forth = j

#  가로 최대값
garo_max = 0
forth = 0
for j in garo_idx:
    back = j - forth
    if back > garo_max:
        garo_max = back
    forth = j

print(garo_max * sero_max)