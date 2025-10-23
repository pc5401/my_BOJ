import sys

def solve(readings):
    cnt = [0] * 1001
    for r in readings:
        cnt[r] += 1

    maxf = max(cnt)
    tops = [i for i in range(1000, 0, -1) if cnt[i] == maxf]

    if len(tops) >= 2:
        return tops[0] - tops[-1]  

    top_val = tops[0]
    secondf = 0
    for i in range(1, 1001):
        if i != top_val and cnt[i] > secondf:
            secondf = cnt[i]

    seconds = [i for i in range(1000, 0, -1) if i != top_val and cnt[i] == secondf]
    
    return max(abs(top_val - seconds[0]), abs(top_val - seconds[-1]))

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    readings = list(map(int, data[1:1+n]))
    print(solve(readings))

if __name__ == "__main__":
    main()
