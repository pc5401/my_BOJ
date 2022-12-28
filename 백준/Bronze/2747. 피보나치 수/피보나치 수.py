arr = [0] * 50
arr[1] = 1

for i in range(2,50):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[int(input())])