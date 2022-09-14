mo = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

word = input()
while word != '#':
    cnt = 0
    for w in word:
        if w in mo:
            cnt += 1
    
    print(cnt)
    word = input()
    