from collections import defaultdict

def solution(nums):
    cnt = len(nums) // 2
    check = defaultdict(bool)
    answer = 0
    for n in nums:
        if cnt ==  0:
            break
            
        if check[n]:
            continue
            
        check[n] = True
        cnt -= 1
        answer += 1
        
    return answer