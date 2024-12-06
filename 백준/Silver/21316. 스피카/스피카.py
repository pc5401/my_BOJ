import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(graph: list[int]) -> int:

    for i in range(1, 12+1):
        if len(graph[i]) == 3:
            lst = [len(graph[j]) for j in graph[i]]
            lst.sort()
            if lst[0] == 1 and lst[1] == 2 and lst[2] == 3:
                return i


    
def main():
    # 입력값
    graph = defaultdict(list)
    for _ in range(12):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)


    # 풀이
    result = solve(graph)
    
    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()