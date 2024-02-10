
def seart(n:int) -> int:
    val = 1
    cnt = 1
    while True:
        if val % n:
            val = val * 10 + 1
            cnt += 1
        else:
            return cnt


if __name__ == '__main__':
    res = []

    while True:
        try:
            n = int(input())
            print(seart(n))

        except EOFError:
            break