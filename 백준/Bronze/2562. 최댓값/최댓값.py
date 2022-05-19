maxV = -1
idx = 0

for tc in range(1, 10):
    response = int(input())
    if response > maxV:
        maxV = response
        idx = tc

print(maxV, idx)