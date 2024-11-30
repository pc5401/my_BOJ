import sys
input = sys.stdin.readline

def solve(N: int, B: list[int]) -> int:
    rtn = 1
    A = set(B)
    
    for a in A:
        lst = [b for b in B if b != a]

        leng = 1
        maxL = 1

        for i in range(1, len(lst)):
            if lst[i] == lst[i-1]:
                leng += 1
                maxL = max(leng, maxL)
            else:
                leng = 1

        rtn = max(maxL, rtn)

    return rtn


    
def main():
    # 입력값
    N = int(input())
    B = [int(input()) for _ in range(N)]

    # 풀이
    result = solve(N, B)

    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()