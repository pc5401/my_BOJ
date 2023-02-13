N = int(input())

def func(n):
    v = str(n)
    for i in v:
        if i == '4' or i == '7':
            continue
        else:
            return False

    return True

for i in range(N,3,-1):
    if func(i):
        res = i
        break

print(res)