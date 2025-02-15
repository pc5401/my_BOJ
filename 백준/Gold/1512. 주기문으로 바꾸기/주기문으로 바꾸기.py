import sys
input = sys.stdin.readline


def solve(M: int, DNA: str) -> int:
    L = len(DNA)
    acgt_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    rtn = float('INF')

    for p in range(1, M+1):
        cost = 0
        for r in range(p):
            acgt = [0, 0, 0, 0] # A, C, G, T 개수

            i = r
            cnt = 0
            while i < L:
                acgt[acgt_idx[DNA[i]]] += 1
                cnt += 1
                i += p
            
            if cnt > 0:
                cost += (cnt - max(acgt))
        rtn = min(rtn, cost)

    return rtn


def main():
    # 입력
    M = int(input())
    DNA = input().rstrip()

    # 풀이
    result = solve(M, DNA)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
