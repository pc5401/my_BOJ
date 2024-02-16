import sys
input = sys.stdin.readline


def solve(lst: list)-> int:
    cnt = 0

    for i in range(1, 20):
        target = lst[i]
        lo, hi = 0, i

        while lo <= hi:
            mid = (lo + hi) // 2
            
            if lst[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        if hi == i:
            continue

        lst[lo], lst[i] = lst[i], lst[lo]
        cnt += 1
        for j in range(i, lo+1, -1):
            cnt += 1
            lst[j], lst[j-1] = lst[j-1], lst[j]

    return cnt



if __name__ == '__main__':
    res = []
    P = int(input())
    
    for _ in range(P):
        T, *lst = map(int, input().split())
        res.append(f'{T} {solve(lst)}')
    
    for r in res:
        print(r)