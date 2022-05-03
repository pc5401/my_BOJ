def func(number):
    lst.append(number)  # 값 넣기
    num = number % 10  # 1의 자리

    for i in range(10): # 0 ~ 9
        if num > i: # 작은 수가 있으면 재귀
            ni = number*10 + i
            func(ni)

N = int(input())  # 입력값
lst = []  # 저장소
for i in range(10):
    func(i)


ans = sorted(lst) # 정렬
print(ans[N] if N < len(lst) else -1)  # 인덱스로 접근 => 출력