import sys
input = sys.stdin.readline

def solve(n, key_1, key_2, cipher):
    idx_map = {w: i for i, w in enumerate(key_1)}
    pi = [idx_map[w] for w in key_2]
    inv = [0] * n
    for i, p in enumerate(pi):
        inv[p] = i
        
    return [cipher[inv[j]] for j in range(n)]

def main():
    # 입력
    T = int(input())
    # 풀이 & 출력
    for _ in range(T):
        n = int(input())
        key_1 = input().split()
        key_2 = input().split()
        cipher = input().split()

        # 풀이
        result = solve(n, key_1, key_2, cipher)

        # 출력
        print(*result)

if __name__ == "__main__":
    main()
