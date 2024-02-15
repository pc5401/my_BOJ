import sys
import math
input = sys.stdin.readline


def solve(x1, y1, r1, x2, y2, r2)-> int:
    
    length = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if length > r1 + r2: # 만나지 않음
        return 0
    elif length == r1 + r2: # 외접
        return 1 
    elif abs(r1-r2) < length < r1 + r2: # 후보가 2개
        return 2 
    elif length == abs(r1 - r2) and length != 0: # 내접도 함
        return 1
    elif length < abs(r1 - r2): # 한 터렛이 다른 터렛 경계 안에 있지만 서로 만나지 않음
        return 0

    return -1


if __name__ == '__main__':
    res = []
    T = int(input())
    lst = [ map(int, input().split()) for _ in range(T)]
    
    for v in lst:
        res.append(solve(*v))

    for r in res:
        print(r)

