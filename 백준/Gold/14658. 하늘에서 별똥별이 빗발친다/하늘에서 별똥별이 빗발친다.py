import sys
input = sys.stdin.readline

def solve(L: int, K: int, stars: list[tuple[int, int]]) -> int:
    # 최대로 튕겨낼 수 있는 별똥별의 개수를 저장하는 변수
    max_bounced = 0
    
    # 별똥별의 위치를 하나씩 순회
    for i in range(K):
        for j in range(K):
            # 현재 트램펄린 위치에서 튕겨낼 수 있는 별똥별의 개수
            count = 0
            # 모든 별똥별에 대해 현재 고려 중인 트램펄린 위치에서 튕겨낼 수 있는지 검사
            for star_x, star_y in stars:
                # 트램펄린의 왼쪽 상단 모서리를 (stars[i][0], stars[j][1])로 설정했을 때,
                # 트램펄린 범위 내에 있는 별똥별이면 count를 증가
                if stars[i][0] <= star_x <= stars[i][0] + L and stars[j][1] <= star_y <= stars[j][1] + L:
                    count += 1
            # 지금까지 고려한 트램펄린 위치 중에서 가장 많은 별똥별을 튕겨낸 경우를 업데이트
            max_bounced = max(max_bounced, count)
    
    # 전체 별똥별 개수에서 최대로 튕겨낼 수 있는 별똥별의 개수를 빼면,
    # 지구에 부딪히는 별똥별의 최소 개수가 됨
    return K - max_bounced

def main():
    # 입력값 받기
    N, M, L, K = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(K)]
    # 문제 해결 후 결과 출력
    print(solve(L, K, stars))

if __name__ == "__main__":
    main()
