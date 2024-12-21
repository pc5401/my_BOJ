import sys
input = sys.stdin.readline

def solve(k: int, words: list[str]) -> int | str:
    
    for i in range(k-1):
        for j in range(i+1, k):
            a = words[i] + words[j]
            b = words[j] + words[i]

            if a == a[::-1]:
                return a
            
            if b == b[::-1]:
                return b

    return 0

if __name__ == "__main__":
    # 입력값
    T = int(input())
    lst = []
    for _ in range(T):
        k = int(input())
        words = [input().rstrip() for _ in range(k)]
        lst.append((k, words))
    
    # 풀이 
    result = [solve(*lst[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(res)