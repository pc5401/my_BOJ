import sys
input = sys.stdin.readline


def search_number(r: int, c: int) -> int:
    if r == 0 and c == 0:
        return 1
    
    level = max(abs(r), abs(c))
    end = (2 * level + 1) ** 2

    # 밑변 확인
    i = level
    for j in range(level, -level-1, -1):
        if i == r and j == c:
            return end
        end -= 1

    # 왼쪽 확인
    for i in range(level-1, -level-1, -1):
        if i == r and j == c:
            return end
        end -= 1
    
    # 위변 확인
    for j in range(-level + 1, level+1, 1):
        if i == r and j == c:
            return end
        end -= 1
    
    # 오른쪽 확인
    for i in range(-level + 1, level, 1):
        if i == r and j == c:
            return end
        end -= 1

    return (2 * level - 1) ** 2 + 1


def search_length(number_table: list[list[int]]) -> int:
    rtn = 0
    for numbers in number_table:
        for number in numbers:
            rtn = max(rtn, len(str(number)))
    return rtn


def solve(num: int, length: int) -> str:
    num_string = str(num)
    cnt = len(num_string)
    if cnt == length:
        return num_string
    
    return ((length - cnt) * ' ') + num_string


def main():
    # 입력값
    r1, c1, r2, c2 = map(int, input().split())
    # 풀이
    number_table = [[search_number(i,j) for j in range(c1, c2 + 1)] for i in range(r1, r2+1)]
    max_len = search_length(number_table)
    result = [[solve(number, max_len) for i, number in enumerate(numbers)] for numbers in number_table]
    # 출력
    for res in result:
        print(*res)

if __name__ == "__main__":
    main()