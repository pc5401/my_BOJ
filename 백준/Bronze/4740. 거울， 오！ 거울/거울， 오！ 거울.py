import sys
input = sys.stdin.readline

result = []
while 1:
    word = input().rstrip('\n')
    if word[0:3] == '***':
        break

    print(word[::-1])

