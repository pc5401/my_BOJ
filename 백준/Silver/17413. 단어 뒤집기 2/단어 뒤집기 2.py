lst = list(input())
n = len(lst)
res = []
alp = []
tags = []
cnt = 0 

for l in lst:
    if l == '>':
        tags.append(l)
        cnt += 1

        if tags and cnt > 2:
            for t in tags:
                res.append(t)
        else:
            for t in tags[::-1]:
                res.append(t)
        cnt = 0
        tags = []
    
    elif l == '<' or cnt:
        if alp:
            for a in alp[::-1]:
                res.append(a)
                alp = []
        tags.append(l)
        cnt += 1

    elif l.isalpha() or l.isdigit():
        alp.append(l)

    else:
        if alp:
            for a in alp[::-1]:
                res.append(a)
                alp = []
        res.append(l)

if alp:
    for a in alp[::-1]:
        res.append(a)

if tags:
    for t in tags:
        res.append(t)

result = "".join(res)
print(result)