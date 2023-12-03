import sys
input = sys.stdin.readline

def find_closest_A(B, N):
    # 시작점 A를 1로 설정
    A = 1
    while True:
        # 현재 A^N 값을 계산
        current_power = A ** N

        # B를 초과하지 않는 최대 A^N을 찾기
        if current_power > B:
            # 이전 A^N과 현재 A^N 중 B에 더 가까운 값을 찾기
            prev_power = (A - 1) ** N
            if abs(prev_power - B) <= abs(current_power - B):
                return A - 1
            else:
                return A

        # A 증가
        A += 1

if __name__ == "__main__":
    while True:
        B, N = map(int, input().split())
        if B == 0 and N == 0:
            break
        print(find_closest_A(B, N))