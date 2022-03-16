#  원래는 eval 함수를 사용해서 풀었다. -> 시간초과
import sys
import itertools

input = sys.stdin.readline

n = int(input())  # 2~11
num_lst = list(map(int, input().split()))  # 수의 순서는 변하지 X
#  0:'+', 1:'-', 2:'*', 3:'/'
operator = list(map(int, input().split()))
opr_lst = ['+']*operator[0] + ['-']*operator[1] + ['*']*operator[2] + ['/']*operator[3]
#  연산자 경우의 수 뽑기
opr_cbi = list(map(list, itertools.permutations(opr_lst, n-1)))

# 최소값, 최대값 구하기
calV = num_lst[0]
minV = 1e10
maxV = -1e10

for lst in opr_cbi:
    calV = num_lst[0]
    for i in range(n-1):

        if lst[i] == '+':
            calV += num_lst[i+1]
        elif lst[i] == '-':
            calV -= num_lst[i+1]
        elif lst[i] == '*':
            calV *= num_lst[i+1]
        elif lst[i] == '/':
            calV = int(calV / num_lst[i+1])

    maxV = max(maxV, calV)
    minV = min(minV, calV)

print(maxV)
print(minV)