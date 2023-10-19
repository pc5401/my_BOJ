import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력 & 전처리
    M = int(input())
    cup = [0,1,0,0]
    for _ in range(M):
        x, y = map(int, input().split())
        cup[x], cup[y] = cup[y], cup[x]
    res = -1
    for i in range(1,4):
        if cup[i]:
            res = i
            break
    print(res)