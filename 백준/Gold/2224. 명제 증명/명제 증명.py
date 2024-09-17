import sys
input = sys.stdin.readline

def get_alphabet() -> list[str]:
    rtn = []

    for i in range(65, 91): # 대문자 A-Z
        rtn.append(chr(i))
    
    for i in range(97, 123): # 소문자 a-z
        rtn.append(chr(i))
    
    return rtn


def solve(graph: dict[str, set]) -> dict[str, set]:
    alphabet = get_alphabet()
    rtn = { alph: set() for alph in alphabet}

    # 기존에 주어진 관계 추가
    for k in graph:
        for v in graph[k]:
            rtn[k].add(v)

    # 플로이드-워셜 방식으로 모든 경로를 찾아냄
    for k in alphabet:
        for i in alphabet:
            for j in alphabet:
                if i != j and j in rtn[k] and k in rtn[i]:
                    rtn[i].add(j)
    
    return rtn


def print_of(result: dict):
    print_lst = []
    alphabet = get_alphabet()

    for x in alphabet:
        lst = list(result.get(x))
        if lst:
            lst.sort()
            for y in lst:
                print_lst.append(f'{x} => {y}')
    
    print(len(print_lst))
    for value in print_lst:
        print(value)


if __name__ == "__main__":
    # 입력값
    N = int(input())
    graph = dict()
    for _ in range(N):
        x, y = input().rstrip().split(' => ')
        if x == y:
            continue

        if graph.get(x):
            graph[x].add(y)
        else:
            graph[x] = {y}


    # 풀이
    result = solve(graph)

    # # 출력
    print_of(result)
