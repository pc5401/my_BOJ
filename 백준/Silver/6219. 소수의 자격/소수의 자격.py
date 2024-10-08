import sys
input = sys.stdin.readline


def solve(A: int, B: int, D: int) -> int:
    # 예라스토체
    dp = [1] * (B+1)
    dp[0], dp[1] = 0, 0

    lst = []

    for i in range(2, B+1):
        if dp[i] == 0:
            continue
        
        if i >= A:
            lst.append(i)

        for j in range(i, B+1, i):
            dp[j] = 0
    
    # 범위 내 수
    cnt = 0
    for n in lst:
        num = n
        while num:
            if num % 10 == D:
                cnt += 1
                break
            
            num //= 10
    
    return cnt
     

if __name__ == "__main__":
    # 입력값
    A, B, D = map(int, input().split())

    # 풀이
    result = solve(A, B, D)

    # 출력
    print(result)