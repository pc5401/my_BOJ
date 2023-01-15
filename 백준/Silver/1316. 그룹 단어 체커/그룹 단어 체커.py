import sys
input = sys.stdin.readline

def check(word):
    chk = []
    for i, w in enumerate(word):
        if w in chk and words[i-1] != w:
            return 0
        chk.append(w)
    return 1

n = int(input())
res = 0
for _ in range(n):
    chk = []
    words = input()
    res += check(words)

print(res)
