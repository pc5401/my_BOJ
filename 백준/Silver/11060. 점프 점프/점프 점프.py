from collections import deque

n = int(input())  # 1~1000
lst = list(map(int, input().split()))  # 0~100

visited = [0] * n
queue = deque([lst[0]])
temp = 0

while queue and n > 1:
    v = queue.popleft()

    for i in range(temp + 1, temp + v + 1):
        if visited[-1] != 0:
            break

        if visited[i] == 0:
            queue.append(lst[i])
            visited[i] = visited[temp] + 1

    if visited[-1] != 0:
        break
    temp += 1

# visited[0] = 1  #  계산 다 끝났으니까. 에지 케이스 1, 1 를 처리하기 위해
res = visited[-1] if visited[-1] != 0 else -1
res = 0 if n == 1 else res
print(res)