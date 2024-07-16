import sys
input = sys.stdin.readline

def solve(T: int):
	t = T
	rtn = 0
	rtn += (t // 600)
	t = (t % 600)

	rtn += (t // 60)
	t = (t % 60)

	if t == 30:
		return rtn + 1
	elif t > 30:
		t -= 30

	rtn += (t // 10)
	t = (t % 10)

	return rtn + 1
	

def main():
	M, S = map(int, input().split(':'))
	print(solve((M*60) + S))

main()