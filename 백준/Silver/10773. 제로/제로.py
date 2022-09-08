K = int(input())

lst = []
for k in range(K):
    ipt = int(input())
    if ipt:
        lst.append(ipt)
    elif not ipt and lst:
        lst.pop()

print(sum(lst))