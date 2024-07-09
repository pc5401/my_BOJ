import sys
input = sys.stdin.readline


def main():
	N = int(input())
	if N == 1:
		print(0)
	elif N % 2:
		print((N*N)//2 + 1)
	else:
		print((N*N)//2)
	
main()