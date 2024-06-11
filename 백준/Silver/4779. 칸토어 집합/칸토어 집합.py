import sys
input = sys.stdin.readline


def solve(lst: list[str]) -> int:
    words = ['-', '- -', '- -   - -', '- -   - -         - -   - -']

    i = 27
    for _ in range(4, 13):
        word = words[-1]
        mid = ' '* len(word)
        words.append(word + mid + word)
    
    return [ words[i] for i in lst]


def main():
    # 입력값
    
    input_lst = []
    while True:
        try:
            input_lst.append(int(input()))
        except:
            break

    # 풀이
    result: list[str] = solve(input_lst)

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
