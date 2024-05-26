import sys
input = sys.stdin.readline


def main():
    # 입력값
    tel_num = [int(input()) for _ in range(4)]
    result = True

    if 8 <= tel_num[0] < 10 and 8 <= tel_num[3] < 10:
        if tel_num[1] == tel_num[2]:
            result = False

    # 출력
    print('answer' if result else 'ignore')
    
if __name__ == "__main__":
    main()