import sys
input = sys.stdin.readline

def solve_tunes(tunes: list[str]) -> list[str]:
    return sorted(tunes, key=lambda s: s.lower())

def main():
    scenario = 1
    while True:
        # 입력
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        tunes = [input().rstrip('\n') for _ in range(n)]
        # 풀이
        sorted_list = solve_tunes(tunes)
        # 출력
        print(scenario)
        for t in sorted_list:
            print(t)
        scenario += 1

if __name__ == "__main__":
    main()
