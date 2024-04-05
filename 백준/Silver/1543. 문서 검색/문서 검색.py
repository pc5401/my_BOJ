import sys
import re
input = sys.stdin.readline


def solve(target: str, words: str) -> int:
    return len(re.findall(re.compile(target), words))


def main():
    # 입력값
    words = input().rstrip()
    target = input().rstrip()
    # 풀이 후, 출력
    print(solve(target, words))


if __name__ == "__main__":
    main()
