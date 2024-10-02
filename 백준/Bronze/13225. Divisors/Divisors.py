import sys
input = sys.stdin.readline

# 약수의 개수를 계산
def solve(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def main():
    # 입력 처리
    C = int(input())  
    lst = [int(input()) for _ in range(C)]
    
    # 풀이
    result = [solve(lst[i]) for i in range(C)]

    # 결과 출력
    for i in range(C):
        print(f"{lst[i]} {result[i]}")

if __name__ == "__main__":
    main()
