import sys
sys.setrecursionlimit(100000)

def func(res:list,arr:list, idx):
    global L, C

    # print(arr)

    if idx > L:
        return

    if len(res) >= L:
        mo = 0
        ja = 0
        for word in res:
            if word in ['a','e','i','o','u']:
                mo += 1
            else:
                ja += 1

            if mo > 0 and ja > 1:
                result.append(res)
                break
        return

    if not arr:
        return

    for i in range(len(arr)):
        res.append(arr[i])
        func(res[:],arr[i+1:], idx+1)
        res.pop()



L, C = map(int, input().split())
input_lst = list(input().split())
lst = sorted(input_lst)
result = []

func([],lst[:], 0)
for r in result:
    print("".join(r))

