import sys
input = sys.stdin.readline


def solve(N, L, K, C, Z) -> str:
    c = C
    attack = [K * min(i + 1, L) for i in range(N)]
    decrement = [0] * (N+1)

    for idx, zombie in enumerate(Z):
        if decrement[idx] > 0:
            attack[idx] -= decrement[idx]
            decrement[idx + 1] += decrement[idx]
        
        if zombie - attack[idx] > 0:
            if C == 0:
                return "NO"
            
            # 지뢰 사용
            C -= 1
            start_decrement = idx + 1
            end_decrement = min(idx + L + 1, N)
            
            decrement[start_decrement] += K
            decrement[end_decrement] -= K  # 누적 감소량을 원복

    return 'YES'


if __name__ == "__main__":
    N = int(input())
    L, K = map(int, input().split())
    C = int(input())
    Z = [int(input()) for _ in range(N)]
    print(solve(N, L, K, C, Z))