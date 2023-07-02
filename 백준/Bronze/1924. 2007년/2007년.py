x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

days = sum(month[:x-1]) + y - 1

print(week[days % 7])