import sys
input = sys.stdin.readline
        
def x(a, c):
    return c - a

def y(a,c):
    return int(c / a)

if __name__ == "__main__":
    # 입력 & 전처리
    ax, ay, az = map(int,input().split())
    cx, cy, cz = map(int,input().split())
    
    print(x(az, cx), y(ay, cy), x(ax, cz))