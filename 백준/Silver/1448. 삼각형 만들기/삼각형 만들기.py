import sys
input = sys.stdin.readline


def look_for_result(n: int, straws: list[int])->int:
    rtn = -1
    for i in range(n-2):
        if straws[i] >= straws[i+1] + straws[i+2]:
            continue
        rtn = max(rtn, (straws[i] + straws[i+1] + straws[i+2]))
    return rtn

def main():
    n = int(input())
    straws = [int(input()) for _ in range(n)]
    straws.sort(reverse=True)

    result = look_for_result(n, straws)
    print(result)


if __name__ == "__main__":
    main()
