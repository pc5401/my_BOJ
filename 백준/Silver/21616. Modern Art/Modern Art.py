import sys
input = sys.stdin.readline

def solve_canvas(M: int, N: int, commands: list) -> int:
    # 0이면 짝수번, 1이면 홀수번
    rows = [0] * M
    cols = [0] * N
    
    for cmd in commands:
        typ, num = cmd.split()
        num = int(num) - 1  # 0-indexed로 변환
        if typ == 'R':
            rows[num] ^= 1  # toggle
        else:
            cols[num] ^= 1  # toggle
    
    r_count = sum(rows)
    c_count = sum(cols)
    gold_cells = r_count * (N - c_count) + (M - r_count) * c_count
    return gold_cells

def main():
    # 입력
    M = int(input())
    N = int(input())
    K = int(input())
    commands = [input().strip() for _ in range(K)]
    
    # 풀이
    result = solve_canvas(M, N, commands)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
