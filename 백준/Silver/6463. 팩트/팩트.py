
import sys
input = sys.stdin.readline

def solve() -> list[int]:
    rtn = [1] * 10001
    n = 1

    for i in range(1, 10001):
        n *= i

        while n % 10 == 0:
            n //= 10
        
        n % 100000
        rtn[i] = n % 10

    return rtn
    

def main():
    table = solve()
    result = []
    data = sys.stdin.read().split()
    for line in data:
        if line.strip() == '':
            continue
        N = int(line)
        result.append(f'{N:5d} -> {table[N]}')
    
    for res in result:
        print(res)

        
if __name__ == '__main__':
    main()