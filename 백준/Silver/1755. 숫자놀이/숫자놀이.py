search = {
    '1':'on', '2':'tw', '3':'th', '4':'fo', '5':'fi', '6':'si', '7':'se', '8':'ei', '9':'ni', '0':'ze'
}
basket = []

M,N = map(int,input().split())
for i in range(M,N+1):
    words = str(i)
    word =''
    for j in words:
        word += search[j]

    basket.append([word, i])

basket.sort(key=lambda x : x[0])

res = []
for b,i in basket:
    res.append(i)

for r in range(0,len(res),10):
    print(*res[r:r+10])