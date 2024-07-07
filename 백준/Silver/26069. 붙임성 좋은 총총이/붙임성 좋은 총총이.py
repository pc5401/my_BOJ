import sys
input = sys.stdin.readline


def main():
	N = int(input())
	lst = {'ChongChong'}
	A = [ input().split() for _ in range(N)]
	for i, j in A:
		if i in lst:
			lst.add(j)
		elif j in lst:
			lst.add(i)
	
	print(len(lst))
	
main()