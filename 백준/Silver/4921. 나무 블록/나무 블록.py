import sys
input = sys.stdin.readline

def solve(n: str):
	lst = list(n)
	data = {
		'1': {'4', '5'},
		'2': {},
		'3': {'4', '5'},
		'4': {'2', '3'},
		'5': {'8'},
		'6': {'2','3'},
		'7': {'8'},
		'8': {'6', '7'}
	}


	if lst[0] != '1' or lst[-1] != '2':
		return False

	for i in range(1, len(lst)):
		b = lst[i-1]
		if not lst[i] in data[b]:
			return False
	
	return True


def main():
	lst = []
	while True:
		n = input().rstrip()
		if n == '0':
			break
		lst.append(n)
	
	result = ['VALID' if solve(n) else 'NOT' for n in lst]
	
	for num, res in enumerate(result, start=1):
		print(f'{num}. {res}')

main()