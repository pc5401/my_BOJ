import sys
input = sys.stdin.readline

def anser(order: str, idx: int) -> str:
    rtn = ''

    for i, word in enumerate(order):

        if i == idx:
            rtn += f'[{word}]'
        else:
            rtn += word
    return rtn


def solve(order: str, options: set) -> str:
    
    if order[0] != ' ' and not order[0].upper() in options:
        options.add(order[0].upper())
        return anser(order, 0)

    for i in range(1, len(order)):
        if order[i-1] == ' ' and not order[i].upper() in options:
            options.add(order[i].upper())
            return anser(order, i)
        
    for i in range(1, len(order)):  
        if order[i] != ' ' and not order[i].upper() in options:
            options.add(order[i].upper())
            return anser(order, i)    
    return order



def main():
    # 입력 처리
    N = int(input())  
    lst = [input().rstrip() for i in range(1, N+1)]
    
    # 풀이
    options = set()
    result = [solve(lst[i], options) for i in range(N)]
    
    
    # 결과 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
