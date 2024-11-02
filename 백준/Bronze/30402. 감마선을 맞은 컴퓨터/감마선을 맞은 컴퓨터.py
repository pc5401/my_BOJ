import sys
input = sys.stdin.readline


def solve(data: list[list[str]]) -> str:
    for d in data:
        if 'w' in d:
            return 'chunbae'
        elif 'b'in d:
            return 'nabi'
        elif 'g'in d:
            return 'yeongcheol'
    return 'w'

if __name__ == "__main__":
    # 입력값
    data = [input().split() for _ in range(15)]
    
    # 풀이
    result = solve(data)
    
    # # 출력
    print(result)