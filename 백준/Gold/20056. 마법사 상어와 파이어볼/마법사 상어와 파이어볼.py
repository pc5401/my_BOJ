import sys
from collections import defaultdict, deque
input = sys.stdin.readline

delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]  # 8 방향값
N, M, K = map(int, input().split())  # N(격자크기), M 파이어볼 수, K 턴 수
balls = defaultdict(deque)  # (딕셔너리 + 데큐)로 접근
for m in range(M):  # 값 받기
    b = list(map(int, input().split()))
    balls[b[0], b[1]].append([b[2], b[3], b[4]])

for _ in range(K):  # K == 명령 횟수
    # 1번 구현
    clone = []  # deepcopy 대신
    for ki in balls:
        if balls[ki] == deque([]):  # 빈 데큐 고려 X
            pass
        else:
            clone.append([ki, len(balls[ki])])  # 길이(clone[1]) 은 복수(4개)의 파이어볼을 처리하기 위해 입력

    for cl in clone:
        for _ in range(cl[1]): # 이동 시키기

            v = balls[cl[0]].popleft()  # 값 빼기

            r, c = cl[0][0], cl[0][1]  # 입력
            m, s, d = v[0], v[1], v[2]

            nr = (r + s * delta[d][0]) % N  # 계산
            nc = (c + s * delta[d][1]) % N

            balls[nr, nc].append([m, s, d])  # 다시 넣기

    # 2번 구현

    clone = []  # deepcopy 대신
    for ki in balls:
        if balls[ki] == deque([]):
            pass
        else:
            if len(balls[ki]) > 1:
                clone.append([ki, len(balls[ki])])

    for cl in clone:

        
        sumM = 0 # 질량 합
        sumS = 0 # 속력 합
        cnt = 0
        flag = [0, 0]  # 홀짝 확인용 ex. sum(flag) == 1 -> 홀홀, 짝짝

        for _ in range(cl[1]):  # 겹치는 애들 빼기

            v = balls[cl[0]].popleft()

            sumM += v[0]
            sumS += v[1]
            cnt += 1

            if v[2] % 2: # 홀수
                flag[0] = 1
            else: # 짝수
                flag[1] = 1

        # 질량이 0 이면
        if not int(sumM/5):  # 질량이 0 이면
            continue

        # 파이어볼 분열
        if sum(flag) == 1: # 모두 같은 방향
            for d_num in [0, 2, 4, 6]:
                balls[cl[0][0], cl[0][1]].append([int(sumM/5), int(sumS/cnt), d_num])

        elif sum(flag) == 2: # 다른 방향
            for d_num in [1, 3, 5, 7]:
                balls[cl[0][0], cl[0][1]].append([int(sumM/5), int(sumS/cnt), d_num])

result = 0
for i in balls:  # 총질량 합하기
    for j in balls[i]:
        result += j[0]

print(result)