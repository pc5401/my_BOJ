T = int(input())
for tc in range(T):
    number = input().rstrip()
    l = len(number)
    if l % 2: a,b = l//2, l//2
    else: a,b = l // 2, (l//2 -1)
    print('Do-it' if number[a] == number[b] else 'Do-it-Not')