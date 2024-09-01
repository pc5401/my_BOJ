import sys
input = sys.stdin.readline

def star_line(i: int, space_len: int, line: str):
    m = space_len - (2 * i)
    return ' ' * i + line + ' ' * m + line


def main():
    # 입력값
    n: int = int(input())
    
    # 풀이
    space_len = (2 * n) - 3
    result = ['*' * n + ' ' * space_len + '*' * n ]
    line = '*' + ' ' * (n-2) + '*'

    for i in range(1, n-1):
        result.append(star_line(i, space_len, line))
    
    # 출력
    for res in result:
        print(res)
    
    print(' ' * (n-1) + line + ' ' * (n-2) + '*')

    for res in result[::-1]:
        print(res)


if __name__ == "__main__":
    main()


