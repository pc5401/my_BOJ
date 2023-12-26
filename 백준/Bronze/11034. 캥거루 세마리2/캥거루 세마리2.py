import sys
input = sys.stdin.readline

if __name__ == "__main__":
    line = []
    while 1:
        value = list(map(int,input().split()))
        if value:
            line.append(value)
        else:
            break
        
    for A, B, C in line:
        
        x = B - A - 1
        y = C - B - 1
        if x > y:
            print(x)
        else:
            print(y)