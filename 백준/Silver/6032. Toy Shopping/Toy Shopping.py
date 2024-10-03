import sys
input = sys.stdin.readline

# 약수의 개수를 계산
def solve(n: int, j: int, p: int) -> int:
    happy_frugal = j / p
    return (n, p, happy_frugal)

def main():
    # 입력 처리
    N = int(input())  
    lst = [solve(i, *map(int, input().split())) for i in range(1, N+1)]
    
    # 풀이
    lst.sort(key=lambda x : -x[2])
    
    result = 0
    for i in range(3):
        result += lst[i][1]
    
    # 결과 출력
    print(result)
    for i in range(3):
        print(lst[i][0])

if __name__ == "__main__":
    main()
