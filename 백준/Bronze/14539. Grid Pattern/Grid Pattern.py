import sys
input = sys.stdin.readline


def solve(N: int, data: list[int]):
    rows, cols, w, h = data
    rtn = [f"Case #{N}:"]

    a = ("+" + "-" * w) * cols + "+"
    b = ("|" + "*" * w) * cols + "|" 

    # 그리드 생성
    for row in range(rows):
        rtn.append(a)
        for _ in range(h):
            rtn.append(b)
    rtn.append(a)

    return "\n".join(rtn)


    
def main():
    # 입력값
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = [solve(i+1, A[i]) for i in range(N)]

    # 결과 출력
    for res in result:
        print(res)

        
if __name__ == '__main__':
    main()