import sys
input = sys.stdin.readline

def solve(T: int, C: int, chores: list[int]) -> int:
    chores.sort()
    total = 0
    cnt = 0
    for t in chores:
        if total + t <= T:
            total += t
            cnt += 1
        else:
            break
    return cnt

def main():
    # 입력
    T = int(input().strip())
    C = int(input().strip())
    chores = [int(input().strip()) for _ in range(C)]
    
    # 풀이
    ans = solve(T, C, chores)
    
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
