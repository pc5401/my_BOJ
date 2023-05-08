a,b = input().split()
alst = list(map(int,a[::-1]))
blst = list(map(int,b[::-1]))
rlst = [0] * (max(len(a),len(b)) + 1) 

for i in range(len(rlst)-1):

    if i < len(alst):
        A = alst[i]
    else:
        A = 0

    if i < len(blst):
        B = blst[i]
    else:
        B = 0
        
    v = A + B + rlst[i]

    if v == 3:
        rlst[i+1] = 1
        rlst[i] = 1
    elif v == 2:
        rlst[i+1] = 1
        rlst[i] = 0
    elif v == 1:
        rlst[i] = 1

res = "".join(map(str,rlst[::-1]))
print(int(res))