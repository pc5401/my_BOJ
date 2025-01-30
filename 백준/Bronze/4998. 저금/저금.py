import sys
input = sys.stdin.read


def solve(N: int, B: int, M: int) -> int:
    year = 0
    deposit = N
    b = (B * 0.01) + 1

    while deposit <= M:
        deposit *= b
        year += 1

    return year

def main():
    # 입력값
    data = input().split('\n')
    
    result = [solve(*map(float, number.split())) for number in data[:-1]]

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()