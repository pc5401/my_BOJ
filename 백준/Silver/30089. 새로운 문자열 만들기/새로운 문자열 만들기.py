import sys
input = sys.stdin.readline


def solve(S: str):
    n = len(S)
    if S == S[::-1]:
        return S
    word = S
    for i in range(n):
        word = S + S[0:i+1][::-1]
        check = True
        for j in range(n):
            if word[-j-1] != S[j]:
                check = False
                break
        
        if check:
            return word
                
    return S + S[::-1]    

def main():
    # 입력값
    T = int(input())
    S = [input().rstrip() for _ in range(T)]
    # 풀이
    result = [solve(s) for s in S]

    # 결과 출력
    for res in result:
        print(res)

        
if __name__ == '__main__':
    main()