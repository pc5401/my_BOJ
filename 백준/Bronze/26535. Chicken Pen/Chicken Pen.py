import sys
import math
input = sys.stdin.readline

def solve(N: int):
    ans = []
    side = int(math.ceil(N**0.5)) + 2
    for i in range(side):
        row = []
        for j in range(side):
            if i == 0 or i == side - 1 or j == 0 or j == side - 1:
                row.append('x')
            else:
                row.append('.')
        ans.append(''.join(row))
    
    return ans

def main():
    # 입력
    N = int(input())

    # 풀이
    result = solve(N)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()