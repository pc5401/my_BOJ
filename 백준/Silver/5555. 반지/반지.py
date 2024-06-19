import sys
input = sys.stdin.readline


def solve(string: str, N: int, rings: list[str]) -> int:
    m = len(string)
    cnt = 0

    for ring in rings:
        i, r = 0, len(ring)
        k = len(ring)
        
        for i in range(r):
            if ring[i] == string[0]:
                v = 1
                for j in range(m):
                    if ring[(i+j) % k] != string[j]:
                        v = 0
                        break
                cnt += v
                if v:
                    break
    
    return cnt


def main():
    # 입력값
    string = input().rstrip()
    N = int(input())
    rings = [input().rstrip() for _ in range(N)]
    
    # 풀이
    result: int= solve(string, N, rings)

    # 출력

    print(result if result != float('INF') else 'stay home')

if __name__ == "__main__":
    main()