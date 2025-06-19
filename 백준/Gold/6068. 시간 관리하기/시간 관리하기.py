import sys
input = sys.stdin.readline

def solve(N: int, tasks: list[tuple[int,int]]) -> int:
    tasks.sort(key=lambda x: x[1])
    curt = 0
    latest = float('inf')
    for t, s in tasks:
        curt += t
        if curt > s:
            return -1
        
        latest = min(latest, s - curt)
    return latest

def main():
    # 입력
    N = int(input().strip())
    tasks = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = solve(N, tasks)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
