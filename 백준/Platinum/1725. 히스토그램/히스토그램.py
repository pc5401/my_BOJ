import sys
input = sys.stdin.readline

def divide_solve(start: int, end: int, lst: list)->int:
    if start == end:
        return 0
    if start + 1 == end:
        return lst[start]
    
    # 1. 히스토그램을 두 부분으로 나눠 경계 찾기
    mid = (start + end) // 2

    # 2. 각 부분에서 가장 큰 직사각형을 찾기 = 이분탐색.
    max_area = max(
        divide_solve(start, mid, lst),
        divide_solve(mid, end, lst)
    )
    
    # 3. 경계선 기준으로 직사각형 중 가장 큰 것을 찾기.
    # 초기화
    left, right = mid - 1, mid # 좌우 : 투포인터
    min_height = min(lst[left], lst[right])
    area_cross = min_height * 2 # 넓이

    while left > start or right < end - 1: # 경계 안 벗어나게 세팅
        if left > start and (right == end - 1 or lst[left - 1] > lst[right + 1]):
            left -= 1
            min_height = min(min_height, lst[left])
        else:
            right += 1
            min_height = min(min_height, lst[right])

        area_cross = max(area_cross, min_height * (right - left + 1))
    
    # 4. 위 세 경우 중 가장 큰 값을 선택합니다.
    max_area = max(max_area, area_cross)

    return max_area

if __name__ == '__main__': # 이분 탐색으로 접근
    N = int(input())
    Arr = [ int(input()) for _ in range(N)]
    print(divide_solve(0, N, Arr))