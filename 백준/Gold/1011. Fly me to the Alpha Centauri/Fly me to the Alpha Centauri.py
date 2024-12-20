import sys
input = sys.stdin.readline

def solve(x: int, y: int) -> int:
    target = y - x
    
    l, v = 1, 1
    
    while target > v:
        l += 1
        n = l // 2
        
        if l % 2:
            v = (n+1)**2
        else:
            v = n * (n+1)

    return l

if __name__ == "__main__":
    # 입력값
    T = int(input())
    lst = [map(int, input().split()) for _ in range(T)]
    
    # 풀이 
    result = [solve(*lst[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(res)
