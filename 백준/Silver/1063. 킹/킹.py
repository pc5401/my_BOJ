import sys
input = sys.stdin.readline
alpa_num = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
num_alpa = '0ABCDEFGH'
delta = {
    'R' :  (1,0), #한 칸 오른쪽으로
    'L' :  (-1,0), #한 칸 왼쪽으로
    'B' :  (0,-1), #한 칸 아래로
    'T' :  (0,1), #한 칸 위로
    'RT' : (1,1), #오른쪽 위 대각선으로
    'LT' : (-1,1), #왼쪽 위 대각선으로
    'RB' : (1,-1), #오른쪽 아래 대각선으로
    'LB' : (-1,-1), #왼쪽 아래 대각선으로
}


king, dol, input_N = input().split() # input 정리 
N = int(input_N)
k = [alpa_num[king[0]],int(king[1])]  # 킹
d = [alpa_num[dol[0]], int(dol[1])]  # 돌

for n in range(N):
    move = input().strip() # 이동 준비
    m = delta[move]
    met = False
    nd = [0,0]
    nk = [k[0] + m[0], k[1] + m[1]] # 킹 이동

    if d[0] == nk[0] and d[1] == nk[1]: # 킹과 돌이 만나면
        nd[0], nd[1] = d[0] + m[0], d[1] + m[1]
        met = True

    if met and 0 < nk[0] < 9 and 0 < nk[1] < 9 and 0 < nd[0] < 9 and 0 < nd[1] < 9: # 체스판 안 나가면
        k = nk
        d = nd # 돌이 만났으니까.

    elif not met and 0 < nk[0] < 9 and 0 < nk[1] < 9: # 돌 안 만났을 경우
        k = nk


res_king = num_alpa[k[0]] + str(k[1])
res_dol = num_alpa[d[0]] + str(d[1])

print(res_king)
print(res_dol)