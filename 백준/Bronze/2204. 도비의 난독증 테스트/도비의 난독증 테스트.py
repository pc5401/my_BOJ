import sys
input = sys.stdin.readline

result = []
while 1:
    n = int(input())
    if n:
        words = []
        value = []
        for i in range(n):
            w = input().rsplit() #split는 리스트로 만든다.
            words.append(w)
            value.append([w[0].upper(),i])
        value.sort()
        print(words[value[0][1]][0])
    else:
        break