import sys
input = sys.stdin.readline


def check_word(A: str, B: str) -> bool:
    m = len(A)
    if m != len(B):
        return False
    
    for i in range(m):
        if B[i] == A[0]:
            flag = True
            for j in range(1, m):
                if B[(i+j) % m] != A[j]:
                    flag = False
                    break
            
            if flag:
                return True
    
    return False


def solve(N: int, lst:list[str]) -> int:
    visited = [0] * N
    cnt = 0

    for i in range(N):
        if visited[i]:
            continue
        cnt += 1
        visited[i] = cnt
        word = lst[i]
        for j in range(i+1, N):
            if check_word(word, lst[j]):
                visited[j] = cnt

    return cnt



def main():
    # 입력값
    N: int = int(input())
    lst: list[str] = [input().rstrip() for _ in range(N)]
    # 풀이
    result: int = solve(N, lst)
    # 출력
    print(result)


if __name__ == "__main__":
    main()