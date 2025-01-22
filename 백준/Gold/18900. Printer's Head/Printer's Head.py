import sys
input = sys.stdin.readline

def solve(n: int, arr: list[int]) -> int:
    pos = [0]*(n+1)
    
    for i, h in enumerate(arr):
        pos[h] = i
    
    arr = [pos[h] for h in range(n, 0, -1)]
    
    cnt = 1
    direct = 0 
    val = arr[0]
    
    for idx in range(1, n):
        x = arr[idx]
        if direct == 0:
            if x > val:
                direct = +1
            elif x < val:
                direct = -1
            else:
                cnt += 1
                direct = 0
            val = x
        else:
            if direct == +1:
                if x > val:
                    val = x
                else:
                    cnt += 1
                    direct = 0
                    val = x
            else:
                if x < val:
                    val = x
                else:
                    cnt += 1
                    direct = 0
                    val = x
    
    return cnt

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(result)

if __name__ == "__main__":
    main()
