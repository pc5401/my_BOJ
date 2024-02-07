import sys
input = sys.stdin.readline


def count_numbers(N: int) -> list:
    """ 입력된 끝 페이지 까지 나온 수의 갯수 
    Arg:
        N (int) : 끝 페이지 번호
    Return:
        list : 끝 페이지 까지 나온 수의 갯수 
    """
    
    count = [0] * 10 # 결과를 저장할 배열 초기화(retunr 값)
    digit = 1 # 시작 자릿수
    
    while N >= digit:
        
        left = N // (digit * 10) # 현재 자릿수의 왼쪽 부분 (+1은 현재 자릿수를 포함하기 위함)
        current = (N // digit) % 10 # 현재 자릿수
        right = N % digit # 현재 자릿수의 오른쪽 부분

        for i in range(10):
            # 현재 자릿수보다 왼쪽에 있는 숫자의 개수
            count[i] += left * digit
            if i < current:
                count[i] += digit
            elif i == current:
                count[i] += right + 1
        
        # 0은 가장 앞자리에 올 수 없으므로, 맨 처음 자릿수를 제외한 경우의 수를 빼줌
        if digit > 1:
            count[0] -= digit
        digit *= 10 # 자리수 증가
    
    count[0] -= 1 # 0이 +1 추가 계산되어서 뺌...
    return count

if __name__ == '__main__':
    N = int(input())
    print(*count_numbers(N))