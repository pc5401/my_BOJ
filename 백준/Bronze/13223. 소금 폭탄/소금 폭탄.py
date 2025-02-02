import sys
input = sys.stdin.readline


def solve(now, salt) -> int:
    h, m, s = now
    now_sec = 3600 * h + 60 * m + s
    h, m, s = salt
    salt_sec = 3600 * h + 60 * m + s
    
    
    if now_sec == salt_sec:
        diff = 24 * 3600
    elif now_sec < salt_sec:
        diff = salt_sec - now_sec
    else:
        diff = 24 * 3600 - (now_sec - salt_sec)

    h = diff // 3600
    diff %= 3600
    m = diff // 60
    s = diff % 60
    
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    # 입력값
    now = map(int, input().split(':'))
    salt = map(int, input().split(':'))
    
    result = solve(now, salt)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
