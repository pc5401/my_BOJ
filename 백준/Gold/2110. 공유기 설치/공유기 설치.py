from typing import List

def is_possible(distance: int, houses: List[int], routers: int) -> bool:
    last_installed = houses[0]  # 첫 번째 집에 공유기 설치
    count = 1  # 설치된 공유기 수
    
    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
            if count >= routers:
                return True
    return False

def find_max_distance(n: int, c: int, houses: List[int]) -> int:
    houses.sort()  # 집의 위치를 정렬
    low, high = 1, houses[-1] - houses[0]  # 가능한 최소 거리와 최대 거리
    
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, houses, c):
            result = mid  # 가능한 경우, 결과 업데이트
            low = mid + 1  # 더 큰 거리 탐색
        else:
            high = mid - 1  # 더 작은 거리 탐색
    
    return result

# 입력 받기
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# 최대 거리 출력
print(find_max_distance(N, C, houses))