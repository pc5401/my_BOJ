import sys
input = sys.stdin.readline


if __name__ == "__main__":
    input_lst = list(map(int,input().split()))
    lst = [0] * 1_000_000
    for num in input_lst:
        i = 1
        val = num *i
        while val < 1_000_000:
            lst[val] += 1
            i += 1
            val = num * i
    res = 0
    for num, cnt in enumerate(lst):
        if cnt > 2:
            res = num
            break
    print(res)

