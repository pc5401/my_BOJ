import sys
input = sys.stdin.readline


def getIdx(S: str) -> int:
    for i in range(len(S)-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'B':
            return i
    
    return -1


def change(idx: int, S: str) -> str:
    return S[:idx] + 'BA' + S[idx+3:]       


def solve(N: int, S: str) -> str:
    result = S
    
    while True:
        idx = getIdx(result)
        if idx == -1:
            break
        result = change(idx, result)
    
    return result
     

if __name__ == "__main__":
    # 입력값
    T = int(input())
    Ns = []
    Ss = []
    for _ in range(T):
        N = int(input())
        S = input().rstrip()
        Ns.append(N)
        Ss.append(S)
        

    # 풀이
    result = [solve(Ns[t], Ss[t]) for t in range(T)]

    # 출력
    for res in result:
        print(res)