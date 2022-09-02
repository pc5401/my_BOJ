N = int(input())
# 1 은 상근이 이김
# 2 는 창영이 이김
# 3~6 번 상근 이김 그리고 8번 창영 이김
# 7, 9 번 창영
value = (N - 2) % 7
res = ''

if value == 0:
    res = 'CY'
elif value == 5:
    res = 'CY'
else:
    res = 'SK'

if N == 1:
    res = 'SK'
elif N == 2:
    res = 'CY'

print(res)