def seach(target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1
        else:
            return 1
    return 0


N = int(input())
Alst = list(map(int, input().split()))
M = int(input())
Mlst = list(map(int, input().split()))  # question
nums = sorted(Alst)  # 이진 탐색을 위한 A 정렬

for m in Mlst:
    left, right = 0, len(nums)
    print(seach(m))