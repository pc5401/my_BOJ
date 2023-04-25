import sys
input = sys.stdin.readline

N, S, P = map(int,input().split())
if N > 0: nlst = list(map(int,input().split())) 
rlst = [i for i in range(1,N+2)]
i = 1 if N > 0 else 0

while i:
    if i >= N or S > nlst[i]: # 마지막
        nlst.insert(i,S)
        if nlst[i] >= nlst[i-1]: rlst[i] = rlst[i-1]
        break

    if nlst[i] == nlst[i-1]: rlst[i] = rlst[i-1]
    
    i += 1

print(rlst[i] if i < P else -1)