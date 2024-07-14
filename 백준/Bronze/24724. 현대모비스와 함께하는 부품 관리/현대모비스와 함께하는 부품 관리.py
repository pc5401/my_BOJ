import sys
input = sys.stdin.readline


def main():
	result = []
	T = int(input())
	for tc in range(T):
		N = int(input())
		A, B = map(int, input().split())
		lst = [list(map(int, input().split())) for _ in range(N)]
		result.append(f'Material Management {tc+1}')
		result.append(f'Classification ---- End!')
	
	for res in result:
		print(res)
main()