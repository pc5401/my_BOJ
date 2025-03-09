import sys
input = sys.stdin.readline

def solve(a: int, b: int, g: int, ta: list[str], tb: list[str], scr: list[str]) -> str:
    setA = set(ta)
    setB = set(tb)
    cntA = cntB = 0
    for s in scr:
        if s in setA:
            cntA += 1
        elif s in setB:
            cntB += 1
    if cntA > cntB:
        return "A"
    elif cntB > cntA:
        return "B"
    else:
        return "TIE"

def main():
    # 입력
    a, b, g = map(int, input().split())
    ta = input().split()
    tb = input().split()
    scr = input().split()
    
    # 풀이
    res = solve(a, b, g, ta, tb, scr)
    
    # 출력
    print(res)

if __name__ == "__main__":
    main()
