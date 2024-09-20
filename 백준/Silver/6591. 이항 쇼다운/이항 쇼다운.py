import sys

def solve(n: int, k: int) -> int:
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result

def main():
    input = sys.stdin.read().split()
    it = iter(input)
    results = []
    
    while True:
        try:
            n = int(next(it))
            k = int(next(it))
            if n == 0 and k == 0:
                break
            results.append(solve(n, k))
        except StopIteration:
            break
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()


