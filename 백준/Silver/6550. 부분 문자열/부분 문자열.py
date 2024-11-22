import sys
input = sys.stdin.read


def solve(s: str, t: str):
    S = list(s[::-1])
    T = list(t[::-1])

    while T and S:
        w = T.pop()
        if S[-1] == w:
            S.pop()

    return 'Yes' if len(S) == 0 else 'No'
    

def main():
    # 입력값
    problems = input().strip().split("\n")

    # 풀이
    result = [solve(*line.split()) for line in problems]

    # 결과 출력
    for res in result:
        print(res)

        
if __name__ == '__main__':
    main()