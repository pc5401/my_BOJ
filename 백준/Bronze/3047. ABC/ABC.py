lst = list(map(int,input().split()))
ABC = list(input())
words = {
    'A':0,'B':1,'C':2
}
lst.sort()

res = []
for v in ABC:
    res.append(lst[words[v]])
print(*res)