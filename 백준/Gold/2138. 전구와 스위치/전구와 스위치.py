import sys
input = sys.stdin.readline

def flip(c):
    return 0 if c == 1 else 1

def simulate_presses(current, target, press_first):
    presses = 0
    current = current[:]  # 리스트를 복사하여 변경 가능하게 만듦
    if press_first:
        current[0] = flip(current[0])
        if N > 1:
            current[1] = flip(current[1])
        presses += 1
    for i in range(1, N):
        if current[i-1] != target[i-1]:
            presses += 1
            current[i-1] = flip(current[i-1])
            current[i] = flip(current[i])
            if i < N-1:
                current[i+1] = flip(current[i+1])
    if current[-1] == target[-1]:
        return presses
    else:
        return float('inf')

def solve(n: int, now: list, target: list):

    # 첫 번째 스위치를 누르는 경우와 누르지 않는 경우를 모두 시뮬레이션
    presses_no_first = simulate_presses(now, target, False)
    presses_with_first = simulate_presses(now, target, True)
    
    # 가능한 최소 횟수를 찾음
    min_presses = min(presses_no_first, presses_with_first)

    return min_presses if min_presses != float('inf') else -1

if __name__ == '__main__':
    # 입력값
    N = int(input())
    start = [int(i) for i in input().rstrip()]
    target = [int(i) for i in input().rstrip()]
    print(solve(N, start, target))