n = int(input())
lst = [input() for i in range(n)]
for i,l in enumerate(lst):
    print(f'{i+1}. {l}')
