# 처음에 회전하고 대칭을 생각하지 않고 간단하게 함수를 5개 만들고 접근
# 알고보니 회전, 대칭을 해야하더라... -> DFS로 4칸 가는거 백트레킹할까 했는데 걍 노가다로 품


import sys
input = sys.stdin.readline



def func0():  # 일자
    maxV = 0
    delta = [[0, 0], [0, 1], [0, 1], [0, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func1():  # 정사각형
    maxV = 0
    delta = [[0, 0], [0, 1], [1, 0], [0, -1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func2():  # ㄴ자
    maxV = 0
    delta = [[0, 0], [0, 1], [-1, -1], [-1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func3():  # 번개모양
    maxV = 0
    delta = [[0, 0], [-1, 0], [1, 1], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV

def func4():  # 버뀨
    maxV = 0
    delta = [[0, 0], [0, -1], [1, 1], [-1, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func5():  # 일자 세우기
    maxV = 0
    delta = [[0, 0], [1, 0], [1, 0], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func6():  # L 2번째
    maxV = 0
    delta = [[0, 0], [1, 0], [-1, 1], [0, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func7():  # L 3번째
    maxV = 0
    delta = [[0, 0], [0, 1], [1, 0], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func8():  # L 4번째
    maxV = 0
    delta = [[0, 0], [0, 1], [0, 1], [-1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func9():  # L 5번째
    maxV = 0
    delta = [[0, 0], [0, 1], [-1, 0], [-1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func10():  # L 6번째
    maxV = 0
    delta = [[0, 0], [-1, 0], [1, 1], [0, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func11():  # L 7번째
    maxV = 0
    delta = [[0, 0], [0, 1], [1, -1], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func12():  # L 8번째
    maxV = 0
    delta = [[0, 0], [0, 1], [0, 1], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func13():  # 번개 2
    maxV = 0
    delta = [[0, 0], [0, 1], [-1, 0], [0, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func14():  # 번개 3
    maxV = 0
    delta = [[0, 0], [1, 0], [0, -1], [1, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func15():  # 번개 4
    maxV = 0
    delta = [[0, 0], [0, 1], [1, 0], [0, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func16():  # ㅗ 2
    maxV = 0
    delta = [[0, 0], [0, -1], [-1, 1], [2, 0]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func17():  # ㅗ 3
    maxV = 0
    delta = [[0, 0], [0, 1], [-1, 0], [1, 1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


def func18():  # ㅗ 4
    maxV = 0
    delta = [[0, 0], [-1, 0], [1, 1], [1, -1]]

    for i in range(N):
        for j in range(M):
            sumV = 0
            ni, nj = i, j
            for d in delta:
                ni = ni + d[0]
                nj = nj + d[1]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[ni][nj]

            maxV = max(maxV, sumV)

    return maxV


# 입력값
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 출력값 세팅
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
func = [func0(), func1(), func2(), func3(), func4(), func5(), func6(), func7(), func8(), func9(), func10(), func11(),
        func12(), func13(), func14(), func15(), func16(), func17(), func18()]
res = 0

for j in range(len(func)):
    result[j] = func[j]
    res = max(result)

print(res)