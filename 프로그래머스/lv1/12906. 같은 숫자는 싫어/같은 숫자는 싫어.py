def solution(arr):
    answer = [v for i,v in enumerate(arr) if i == 0 or arr[i-1] != arr[i]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer