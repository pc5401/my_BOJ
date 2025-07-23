import sys
input = sys.stdin.readline

def solve(nums: list[int]) -> int:
    G = len(nums)
    if G == 1:
        return 1  
    
    m = G
    while True:
        seen = set()
        collision = False
        for x in nums:
            r = x % m
            if r in seen:
                collision = True
                break
            seen.add(r)
        if not collision:
            return m
        m += 1

def main():
    T = int(input())
    for _ in range(T):
        G = int(input())
        students = [int(input()) for _ in range(G)]
        print(solve(students))

if __name__ == "__main__":
    main()
