import sys
input = sys.stdin.readline


if __name__ == "__main__":
    now = list(map(int, input().split(':')))
    start = list(map(int, input().split(':')))
    now_sec = now[0]*3600 + now[1]*60 + now[2]
    start_sec = start[0]*3600 + start[1]*60 + start[2]
    second = start_sec - now_sec

    if second < 0: # 음수
        second += 86400

    hour = str(second // 3600) if second // 3600 > 9 else '0' + str(second // 3600)
    second = second % 3600

    minute = str(second // 60) if second // 60 > 9 else '0' + str(second // 60)
    second = second % 60

    second = str(second)if second > 9 else '0' + str(second)
    print(f'{hour}:{minute}:{second}')
