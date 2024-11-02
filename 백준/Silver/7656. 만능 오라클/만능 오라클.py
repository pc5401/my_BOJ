import sys
input = sys.stdin.readline

def solve(questions: str):
    rtn = []
    start = end = -1
    while True:
        start = questions.find('What is', end + 1)
        if start == -1:
            break
        end = questions.find('?', start)
        if end == -1:
            break

        if '.' in questions[start:end]:
            end = questions.find('.', start)
            continue

        answer = 'Forty-two' + questions[start + 4:end] + '.'
        rtn.append(answer)

    return rtn


if __name__ == "__main__":
    # 입력값
    questions = input().rstrip()
    
    # 풀이
    result = solve(questions)
    
    # 출력
    for res in result:
        print(res)

