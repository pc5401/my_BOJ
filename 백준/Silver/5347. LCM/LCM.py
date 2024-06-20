import sys
import math
input = sys.stdin.readline

def main():
    # 입력값 및 풀이
    N = int(input())
    numbers = [math.lcm(*map(int, input().split())) for _ in range(N)]
    
    # 출력
    for res in numbers:
        print(res)

if __name__ == "__main__":
    main()