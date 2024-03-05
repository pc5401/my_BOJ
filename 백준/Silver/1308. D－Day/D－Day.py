import sys
import datetime
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))

    remaining =  datetime.datetime(d_day[0], d_day[1], d_day[2]) - datetime.datetime(today[0], today[1], today[2])

    print(f'D-{remaining.days}' if datetime.datetime(today[0]+1000, today[1], today[2]) > datetime.datetime(d_day[0], d_day[1], d_day[2]) else 'gg')
