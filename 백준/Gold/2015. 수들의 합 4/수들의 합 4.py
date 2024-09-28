import sys
input = sys.stdin.readline

from collections import defaultdict

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    count = 0
    current_sum = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1 
    
    for i in range(N):
        current_sum += A[i]
        if current_sum - K in prefix_sums:
            count += prefix_sums[current_sum - K]
        prefix_sums[current_sum] += 1
    
    print(count)
