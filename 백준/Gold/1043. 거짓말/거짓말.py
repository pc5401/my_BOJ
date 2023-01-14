from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N_lst = [1] * (N+1) # 진실을 모르는 사람
M_lst = [1] * (M+1) # 진실을 모르는 파티
N_lst[0] = 0
M_lst[0] = 0
true_lst = list(map(int,input().split()))

party = [[0]]
p = defaultdict(list) # 간 파티 정보

for i in range(1,M+1):
    V = list(map(int,input().split()))
    party.append(V)
    for v in V[1:]:
        p[v].append(i)

Q = deque() # 진실과 연결된 사람
if true_lst[0]:
    for t in true_lst[1:]:
        Q.append(t)
else:
    print(M)
    exit()

while Q:
    v = Q.popleft()

    if N_lst[v] == 0: # 안전 장치
        continue
    N_lst[v] = 0
    
    for i in p[v]: # pop이 간 파티
        if M_lst[i]: # 파티를 탐색했는지
            M_lst[i] = 0

            for j in party[i][1:]: # 탐색 안 했다면 순회
                if N_lst[j]: 
                    Q.append(j)

print(sum(M_lst))  # 결과
