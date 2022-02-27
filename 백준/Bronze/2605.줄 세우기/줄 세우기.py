#입력 처리
T = int(input())
lst = list(map(int, input().split()))

# index는 1부터, 리스트에 맨뒤로 밀린 값 삭제
arr = [0]*T
for x, y in enumerate(lst, start=1):
    arr.insert(y, x)
    arr.pop()

for i in arr[::-1]:
    print(int(i), end=" ")
