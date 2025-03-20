import sys
input = sys.stdin.readline

def solve(N: int, dates: list[str]) -> list[str]:
    haab = ["pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", "yax", "zac", "ceh", "mac", "kankin", "muan", "pax", "koyab", "cumhu", "uayet"]
    tzolkin = ["imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", "ok", "chuen", "eb", "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"]
    
    result = []
    for date in dates:
        parts = date.split()
        day = int(parts[0][:-1])
        month = parts[1]
        year = int(parts[2])
        
        idx = haab.index(month)
        total = year * 365 + idx * 20 + day
        
        tz_year = total // 260
        remain = total % 260
        tz_day_num = remain % 13 + 1
        tz_day_name = tzolkin[remain % 20]
        
        result.append(f"{tz_day_num} {tz_day_name} {tz_year}")
    return result

def main():
    # 입력
    N = int(input().strip())
    dates = [input().strip() for _ in range(N)]
    
    # 풀이
    result = solve(N, dates)
    
    # 출력
    print(N)
    for res in result:
        print(res)

if __name__ == "__main__":
    main()