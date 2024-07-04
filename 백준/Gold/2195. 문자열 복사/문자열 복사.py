def solve(S, P):
    n, m = len(S), len(P)
    i = 0
    count = 0
    
    while i < m:
        # 찾을 수 있는 최대 길이의 부분 문자열을 찾는다.
        max_len = 0
        for j in range(n):
            if S[j] == P[i]:
                length = 0
                while j + length < n and i + length < m and S[j + length] == P[i + length]:
                    length += 1
                max_len = max(max_len, length)
        
        # 찾은 최대 길이만큼 이동
        i += max_len
        count += 1
    
    return count

# 입력 받기
S = input().strip()
P = input().strip()

# 결과 출력
print(solve(S, P))
