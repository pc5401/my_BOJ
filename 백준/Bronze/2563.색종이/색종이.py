n = int(input())
lst = [[0 for i in range(100)] for j in range(100)]
for tc in range(1, n+1):
    col, row = map(int, input().split())

    for i in range(row, row+10):
        lst[i][col:col+10] = [1]*10

result = 0
for k in lst:
    result += k.count(1)

print(result)