lst = [int(input()) for _ in range(4)]

res = [''] * 3
for i in range(1,4):
    if lst[i] > lst[i-1]:
        res[i-1] = 'up'
    elif lst[i] == lst[i-1]:
        res[i-1] = 'same'
    elif lst[i] < lst[i-1]:
        res[i-1] = 'down'

if res[0] == res[1] and res[1] == res[2] and res[0] == 'up':
    print('Fish Rising')
elif res[0] == res[1] and res[1] == res[2] and res[0] == 'same':
    print('Fish At Constant Depth')
elif res[0] == res[1] and res[1] == res[2] and res[0] == 'down':
    print('Fish Diving')
else:
    print('No Fish')