import sys
import math
input = sys.stdin.readline

def solve(test_idx: int, N: int) -> str:
    if test_idx % 69 == 0:
        return "AMPPZ 2010"
    
    val = 3 * N / 7
    age = math.floor(val + 0.5)
    return str(age)

def main():
    # 입력
    data = sys.stdin.read().split()
    T = int(data[0])
    Ns = list(map(int, data[1:1+T]))
    
    #풀이
    results = []
    for i, N in enumerate(Ns, start=1):
        results.append(solve(i, N))
    
    #출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
