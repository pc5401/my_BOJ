import sys
input = sys.stdin.readline

S = input()
v =S[0]
z,o=0,0
if v == '0':
    z += 1
else:
    o += 1

for s in S:
    if s != v and s == '0':
        z += 1
        v = s
    elif s != v and s == '1':
        o += 1
        v = s


print(min(z,o))
