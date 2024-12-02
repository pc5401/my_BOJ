import sys
from collections import deque
input = sys.stdin.read

def solve(N: int, nums: list[int]) -> int:
    cnt = 0
    vistied = [0] * N

    for i in range(N):
        if vistied[i]:
            continue
        cnt += 1
        
        j = i
        while not vistied[j]:
            vistied[j] = 1
            j = nums[j] - 1

    return cnt


    
def main():
    # 입력값
    data = input().split('\n')
    T = int(data[0])

    # 풀이
    result = [solve(int(data[i]), list(map(int, data[i+1].split()))) for i in range(1, 2*T+1, 2)]

    # 결과 출력
    for res in result:
        print(res)
        
if __name__ == '__main__':
    main()