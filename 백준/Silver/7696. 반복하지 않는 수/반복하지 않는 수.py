import sys
from itertools import permutations

def build():
    digits = list(range(10))
    a = []
    for k in range(1, 8):
        a_append = a.append
        for p in permutations(digits, k):
            if p[0] == 0:
                continue
            val = 0
            for d in p:
                val = val * 10 + d
            a_append(val)
    a.sort()
    if len(a) >= 1000000:
        return a[:1000000]
    b = []
    for p in permutations(digits, 8):
        if p[0] == 0:
            continue
        val = 0
        for d in p:
            val = val * 10 + d
        b.append(val)
    b.sort()
    c = []
    i = 0
    j = 0
    c_append = c.append
    while len(c) < 1000000:
        if i >= len(a):
            c_append(b[j])
            j += 1
        elif j >= len(b):
            c_append(a[i])
            i += 1
        else:
            if a[i] < b[j]:
                c_append(a[i])
                i += 1
            else:
                c_append(b[j])
                j += 1
    return c

def main():
    arr = build()
    data = map(int, sys.stdin.read().strip().split())
    for n in data:
        if n == 0:
            break
        print(arr[n-1])

if __name__ == "__main__":
    main()
