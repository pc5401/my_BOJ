import collections

def dfs(val: list, ports: list, vis: list, ans: list):
    
    if not ports:
        ans.append(vis[:])
        return 
    
    for i,v in enumerate(ports):
        if v[0] == val[1]:
            lst = ports[:]
            lst.pop(i)
            vis.append(v[1])
            res = dfs(v,lst,vis,ans)
            vis.pop()

def solution(tickets):
    answer = []
    tickets.sort()
    visit = ['ICN']
    for i,v in enumerate(tickets):
        if v[0] == 'ICN':
            lst = tickets[:]
            lst.pop(i)
            visit.append(v[1])
            dfs(v,lst, visit, answer)
            visit.pop()
        
    return answer[0]