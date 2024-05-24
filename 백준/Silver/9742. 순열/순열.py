import sys
input = sys.stdin.readline

def step_fun(target: int, m: int, top: int, nums: list):
    if m == 0:
        return nums

    step = top // m
    value, floor = 0, 0
    while target > value:
        value += step
        floor += 1

    nums.append(floor - 1)
    return step_fun(target + step - value, m - 1, step, nums)

def solve(data: list[tuple[str, int]], dp: list[int]) -> list[str]:
    rtn = []
    for lst, n in data:
        m = len(lst)
        if n > dp[m]:
            rtn.append(f'{lst} {n} = No permutation')
            continue

        nums = step_fun(n, m, dp[m], [])
        word = ''
        queue = list(lst)
        for num in nums:
            if num >= len(queue):
                rtn.append(f'{lst} {n} = No permutation')
                break
            word += queue.pop(num)
        else:
            rtn.append(f'{lst} {n} = {word}')

    return rtn

def main():
    # 입력값
    data = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            A, B = line.split()
            data.append((A, int(B)))
        except (EOFError, ValueError):
            break

    # 풀이
    dp = [1]
    for i in range(1, 11):
        dp.append(dp[-1] * i)

    result: list[str] = solve(data, dp)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
