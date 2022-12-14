word = input()
l = len(word)
res = []


for i in range(1,l-1):
    for j in range(i+1,l):
        a = word[0:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        v = "".join([a,b,c])
        res.append(v)

res.sort()
print(res[0])