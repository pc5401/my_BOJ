import sys
input = sys.stdin.readline

N = int(input()) # 사진 틀 갯수
rcm = int(input()) # 추천 횟수
lst = list(map(int,input().split())) # 추천
note = [0] * (rcm + 1) # 추천 학생 기록
res = []

for i in range(rcm):
    v = lst[i] # 추천 받은 놈
    
    if note[v] == 0 and len(res) >= N:
        idx = 0
        minV = note[res[0]]
        for j in range(len(res)):
            if note[res[j]] < minV: # 뺄 녀석
                idx = j
                minV = note[res[j]]
        note[res.pop(idx)] = 0 # 삭제 및 추천 0 처리
        note[v] = 1
        res.append(v)
    
    elif note[v] == 0 and len(res) < N:
        res.append(v)
        note[v] = 1
    
    elif note[v]:
        note[v] += 1
    # print(f'note : {note} res : {res}')

print(*sorted(res))