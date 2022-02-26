# 입력 처리

n, m = map(int, (input().split()))
srh = list(map(int, (input().split())))

lst = list(range(1, n+1))
number = 0

#앞뒤 경로 카운트
for i in srh:
    if lst[0] == i:
        lst.pop(0)
    else:
        cnt = 0
        pro = 0
        bak = 0
        for j in lst:
            if i == j:
                pro += cnt
                cnt = 1
                break
            else:
                cnt += 1

        for k in lst[::-1]:
            if i == k:
                bak += cnt
                cnt = 0
                break
            else:
                cnt += 1

        # 앞뒤 비교 & 리스트 정렬
        if bak >= pro:
            number += pro
            new_lst = lst[pro:]
            new_lst.extend(lst[:pro])
            new_lst.pop(0)
            lst = new_lst

        else:
            number += bak
            new_lst = lst[-bak:]
            new_lst.extend(lst[:-bak])
            new_lst.pop(0)
            lst = new_lst

print(number)