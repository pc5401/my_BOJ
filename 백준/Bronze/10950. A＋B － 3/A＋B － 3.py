T = int(input())
lst = []
for tc in range(T):
    a, b = map(int, input().split())
    lst.append(a+b)

for l in lst:
    print(l)