# 입력 받기
time1 = int(input())
time2 = int(input())
time3 = int(input())
time4 = int(input())

# 총 이동 시간 계산
total_seconds = time1 + time2 + time3 + time4

# 분과 초로 변환
minutes = total_seconds // 60
seconds = total_seconds % 60

# 출력
print(minutes)
print(seconds)
