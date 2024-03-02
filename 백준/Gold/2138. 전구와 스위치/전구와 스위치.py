import sys
input = sys.stdin.readline


def simulate_presses(now, target, press_first):
    presses = 0
    btn = now[:]  # 리스트를 복사하여 변경 가능하게 만듦
    
    if press_first: # 첫 번째 버튼 누른 경우, 초기화
        btn[0] = (btn[0]+1) % 2
        if N > 1:
            btn[1] = (btn[1]+1) % 2
        presses += 1
    
    # 반복문으로 누른 경우 확인
    for i in range(1, N):
        # 현재 위치에서 이전 버튼이 target과 다르면, 눌러!
        if btn[i-1] != target[i-1]:
            presses += 1
            btn[i-1] = (btn[i-1] + 1) % 2
            btn[i] = (btn[i] + 1) % 2
            if i < N-1: # 경계값 확인
                btn[i+1] = (btn[i+1] + 1) % 2
    
    if btn[-1] == target[-1]: # 유효한지 아닌지.
        return presses
    else:
        return float('inf')

def solve(n: int, now: list, target: list):

    # 첫 번째 스위치를 누르는 경우와 누르지 않는 경우를 모두 시뮬레이션
    # 즉, for문을 두 번 돌린다.
    not_press_first = simulate_presses(now, target, False)
    yes_press_first = simulate_presses(now, target, True)
    
    # 가능한 최소 횟수를 찾음
    min_presses = min(not_press_first, yes_press_first)
    
    return min_presses if min_presses != float('inf') else -1

if __name__ == '__main__':
    # 입력값
    N = int(input())
    start = [int(i) for i in input().rstrip()]
    target = [int(i) for i in input().rstrip()]
    print(solve(N, start, target))