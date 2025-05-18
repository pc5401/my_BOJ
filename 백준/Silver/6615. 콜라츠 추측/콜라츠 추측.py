import sys
input = sys.stdin.readline

def solve(A: int, B: int) -> tuple[int,int,int]:
    stepsA = {}
    x = A
    step = 0
    while True:
        if x not in stepsA:
            stepsA[x] = step
        if x == 1:
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        step += 1
    # B 경로 따라가며 만나는 값 찾기
    y = B
    stepB = 0
    while True:
        if y in stepsA:
            return stepsA[y], stepB, y
        if y == 1:
            # 1은 A 경로에도 있으니 여기서도 만남
            return stepsA[1], stepB, 1
        if y % 2 == 0:
            y //= 2
        else:
            y = 3*y + 1
        stepB += 1

def main():
    # 입력
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        # 풀이
        SA, SB, C = solve(A, B)
        # 출력
        print(f"{A} needs {SA} steps, {B} needs {SB} steps, they meet at {C}")

if __name__ == "__main__":
    main()
