import sys
#  입력처리
num = int(sys.stdin.readline())
# 일단 빈 gird 만들기
grid = [[0 for i in range(1001)] for j in range(1001)]
# 색종이 붙이기
for n in range(1, num+1):
    x, y, w, h = map(int, sys.stdin.readline().split())

    for i in range(y, y+h):
        # for i in range(y, y+h):  # 1 번 시도 : 53점
        #     grid[i][j] = n
        grid[i][x:x+w] = [n]*w  # 2번 시도 : 53 점 => 입력 속도가 미세하게 줄었다.

# 색종이 면접 계산(출력)
for n in range(1, num+1):
    n_sum = 0
    # for i in range(1001):  # 3 번째 출력도 이중 for 문이다.
    #     for j in range(1001):
    #         if grid[i][j] == n:
    #             n_sum += 1
    #         else:
    #             pass
    for g in grid:  # 카운트 함수 활용
        n_sum += g.count(n)
            
    print(n_sum)
    # 시간 못 줄이겠다.