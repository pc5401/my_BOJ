dise = {3:'A',2:'B',1:'C',0:'D',4:'E'}
res = []
for _ in range(3):
    v = sum(list(map(int,input().split())))
    print(dise[v])
