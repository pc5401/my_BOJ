S = list(input())
T = list(input())
s = "".join(S)
n = len(S)

def func(t):
    global result

    if len(t) == n and "".join(t) == s:
        result = 1
        return

    elif len(t) <= n:
        return

    if t[-1] == 'A':
        func(t[:-1])

    if t[0] == 'B':
        tB = t[1:]
        func(tB[::-1])



result = 0
func(T)
print(result)