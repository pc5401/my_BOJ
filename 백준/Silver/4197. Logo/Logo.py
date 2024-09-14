import sys
import math
input = sys.stdin.readline

def solve(n: int, lst: list[str]) -> int:
    x, y, angle = 0, 0, 0

    for act, num in lst:
        num = int(num)
        if act == 'fd':
            # 현재 각도에 맞게 앞으로 이동 (라디안으로 변환해서 cos, sin 사용)
            x += num * math.cos(math.radians(angle))
            y += num * math.sin(math.radians(angle))
        elif act == 'bk':
            # 현재 각도에 맞게 뒤로 이동
            x -= num * math.cos(math.radians(angle))
            y -= num * math.sin(math.radians(angle))
        elif act == 'lt':
            # 왼쪽으로 회전 (각도 증가)
            angle += num
        elif act == 'rt':
            # 오른쪽으로 회전 (각도 감소)
            angle -= num
    
    rtn = math.sqrt(x**2 + y**2)
    return round(rtn)

if __name__ == "__main__":
    result = []
    tc = int(input())
    for t in range(tc):
        n = int(input())
        result.append(solve(n, [input().split() for _ in range(n)]))
    
    for res in result:
        print(res)

