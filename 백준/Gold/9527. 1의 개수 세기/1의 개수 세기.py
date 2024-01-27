import sys
input = sys.stdin.readline


def count_ones(N):
        # N이 0이거나 1인 경우를 처리
        if N <= 1:
            return N
        # 가장 높은 자리수의 1 찾기
        # bit_length() : 파이썬의 내장 함수로, 주어진 정수를 이진수로 표현했을 때 필요한 비트의 최소 개수를 반환
        L = N.bit_length() - 1 
        # 해당 자리수 이하의 모든 숫자에 대한 1의 총 개수 계산
        count = (1 << L) // 2 * L
        # 남은 숫자에 대한 1의 개수 계산
        remainder = N - (1 << L)
        return count + remainder + 1 + count_ones(remainder)

if __name__ == '__main__':
    A, B = map(int,input().split())
    print(count_ones(B) - count_ones(A - 1))