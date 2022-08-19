from collections import defaultdict

def mode_func(lst:list):
    dct = defaultdict()

    for l in lst:
        if l in dct:
            dct[l] += 1
        else:
            dct[l] = 1
    maxV = 0
    res = []
    for d in dct:
        item = dct[d]
        if item > maxV:
            maxV = item
            res= []
            res.append(d)
        elif item == maxV:
            res.append(d)
    
    if len(res) == 1:
        return res[0]

    else:
        result = sorted(res)
        return result[1]

N = int(input())
lst = [int(input()) for _ in range(N)]

arg_v = round(sum(lst) / N)
mid_lst = sorted(lst)
mid_v = mid_lst[(N-1)//2]
mode_v = mode_func(lst)
arange_v = max(lst) - min(lst)

print(arg_v)
print(mid_v)
print(mode_v)
print(arange_v)