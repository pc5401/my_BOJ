import sys, itertools
input = sys.stdin.readline

def solve(time_str: str) -> int:
    parts = time_str.split(':')
    count_valid = 0
    # 모든 순열 (총 6개)
    for perm in itertools.permutations(range(3), 3):
        hour = int(parts[perm[0]])
        minute = int(parts[perm[1]])
        second = int(parts[perm[2]])
        if 1 <= hour <= 12 and 0 <= minute <= 59 and 0 <= second <= 59:
            count_valid += 1
    return count_valid

def main():
    # 입력
    time_str = input().strip()
    
    # 풀이
    result = solve(time_str)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
