import sys
input = sys.stdin.readline

def solve(digits: list[int]) -> int:
    if 0 not in digits:
        return -1
                
    if sum(digits) % 3 != 0:
        return -1
    
    digits.sort(reverse=True)
    return ''.join(map(str, digits))


def main():
    # 입력
    N = input().strip()
    
    # 풀이
    result = solve(list(map(int, N)))
    
    # 출력
    print(result)


if __name__ == "__main__":
    main()