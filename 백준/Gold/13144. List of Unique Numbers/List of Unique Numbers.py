import sys
input = sys.stdin.readline

def look_for_result(n: int, numbers: list[int])->int:
    cnt = 0
    start, end = 0, 0
    data = set()

    while end < n:
        if numbers[end] in data:
            while numbers[start] != numbers[end]:
                data.remove(numbers[start])
                start += 1
            start += 1
        else:
            data.add(numbers[end])
        cnt += (end - start + 1)
        end += 1
    return cnt


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    result = look_for_result(n, numbers)
    print(result)


if __name__ == "__main__":
    main()
