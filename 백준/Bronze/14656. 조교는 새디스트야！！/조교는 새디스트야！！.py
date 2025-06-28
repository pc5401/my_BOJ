import sys
tokens = sys.stdin.read().split()
nums = map(int, tokens[1:])
# 맞지 않는 경우를 1로 세어서 합산
print(sum(1 for i, v in enumerate(nums, 1) if i != v))
