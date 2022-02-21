n = int(input())
lst = list(map(int, input().split()))
num_of_std = int(input())

for _ in range(num_of_std):
    std_gen, idx = map(int, input().split())

    #  남학생
    if std_gen == 1:
        for i in range(idx-1, n, idx):
            if lst[i] == 0:
                lst[i] = 1
            elif lst[i] == 1:
                lst[i] = 0
            else:
                pass  #  반례는 없겠지?

    #  여학생
    if std_gen == 2:
        if lst[idx-1] == 0: # 본인 idx는 무조건 변환
            lst[idx-1] = 1
        else:
            lst[idx-1] = 0

        m = 1
        while idx-1 - m >= 0 and idx-1 + m < n:  # 범위 조건 지정
            if lst[idx-1-m] == lst[idx-1+m]:  # 대칭 확인
                if lst[idx-1-m] == 0:
                    lst[idx-1 - m], lst[idx-1 + m] = 1, 1
                else:
                    lst[idx-1 - m], lst[idx-1 + m] = 0, 0
            else:  # 대칭이 아니라면
                break
            m += 1

#  출력 처리
for i in range(1, n+1):
    if i % 20 == 0:
        print(lst[i-1])
    else:
        print(lst[i-1], end=' ')