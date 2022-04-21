import sys
input = sys.stdin.readline

def packing(wlst,vlst):  # 2차원 배열을 만든다.
    arr = [[0 for i in range(K+1)] for j in range(N+1)]
    for vl in range(N+1):  # 행 가치
        for wt in range(K+1):  # 열 무게
            if vl == 0 or wt == 0:
                arr[vl][wt] = 0
            elif wlst[vl-1] <= wt:
                arr[vl][wt] = max(vlst[vl-1]+arr[vl-1][wt-wlst[vl-1]], arr[vl-1][wt])
            else:
                arr[vl][wt] = arr[vl-1][wt]

    return arr[N][K]

N, K = map(int, input().split()) # N:물품 수, K:무게
wlst = []  # 무게 저장소
vlst = []  # 가치 저장소

for i in range(N):
    w, v = map(int, input().split())
    wlst.append(w)
    vlst.append(v)

print(packing(wlst, vlst))