import sys
input = sys.stdin.readline

def is_matching(number: str, query: str, a: int, b: int) -> bool:
    b_cnt = [0] * 4
    for i in range(4):
        if number[i] == query[i]:
            b_cnt[i] = 1

    if sum(b_cnt) != b:
        return False
    
    a_cnt = [0] * 4
    for num in number:
        for i in range(4):
            if num == query[i] and a_cnt[i] == 0:
                a_cnt[i] = 1
                break
    
    if sum(a_cnt) != a:
        return False
    return True



def solve(N: int, data: list[str]) -> list[str]:
    rtn = []
    
    for i in range(10000):
        number = '{0:04d}'.format(i)
        flag = True
        for query, a, b in data:
            if not is_matching(number, query, int(a), int(b)):
                flag = False
                break
        
        if flag:
            rtn.append(number)

    return rtn

def main():
    # 입력
    N = int(input())
    data = [input().split() for _ in range(N)]

    # 풀이
    result = solve(N, data)

    # 출력
    print(len(result))
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
