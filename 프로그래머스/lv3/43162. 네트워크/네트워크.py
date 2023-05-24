def dfs(num:int, visit:list, computers:list):
    visit[num] = 1
    
    for i,v in enumerate(computers[num]):
        if v and not visit[i]:
            dfs(i,visit,computers)
            

def solution(n, computers):
    answer = 0
    visit = [0] * n
    for i in range(n):
        if visit[i]:
            continue
        dfs(i,visit,computers)
        answer += 1
    return answer