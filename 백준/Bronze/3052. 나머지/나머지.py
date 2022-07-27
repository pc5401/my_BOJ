lst = set()

for i in range(10):
    n = int(input())
    lst.add(n%42)

print(len(lst))