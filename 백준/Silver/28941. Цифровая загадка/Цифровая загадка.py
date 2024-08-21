import sys
input = sys.stdin.readline
    
def count_num(n: int, nums:dict[int, list]):
    key_value = 1
    Q = list(str(n))

    while Q:
        v = Q.pop()
        if nums.get(key_value):
            nums[key_value].append(int(v))
        else:
            nums[key_value] = [int(v)]
        key_value *= 10



def solve(n: int, k: int, a: list[int]) -> int:
    rtn = 0

    nums = {}
    for num in a:
        count_num(num, nums)

    nums_keys = list(nums)
    nums_keys.sort(reverse=True)
    
    for key in nums_keys:
        values = nums[key]
        values.sort()
        for value in values:
            if value == 9:
                break
            rtn += ((9-value) * key)
            k -= 1
            if k <= 0:
                return rtn

    return rtn



def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(n, k, a))


main()


