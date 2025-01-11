import sys
input = sys.stdin.readline


def solve(W: str) -> str:
    state = 0
    count = 0

    for ch in W:
        if state == 0:
            if ch == 'o':
                state = 1
        elif state == 1:
            if ch == 'i':
                state = 2
        else:
            if ch == 'j':
                count += 1
                state = 0 

    if count == 0:
        return "NIE"
    else:
        return str(count)




if __name__ == '__main__':
    # 입력값
    W = input().rstrip()
    
    # 풀이
    result = solve(W)

    # 출력
    print(result)
    