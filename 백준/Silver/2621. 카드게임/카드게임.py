import sys
import collections
input = sys.stdin.readline


def solve(deck: list[tuple[str, int]]) -> tuple[int, int]:
    color = [ c for c, n in deck]
    number = [ n for c, n in deck]
    same_color = False
    same_number = True
    
    # 같은 색상
    if all([color[0] == color[i] for i in range(1,5)]):
        same_color = True
    
    # 연속 숫자
    sorted_number = sorted(number)
    for i in range(1, 5):
        if sorted_number[i] != sorted_number[i-1] + 1:
            same_number = False
            break
    
    # 숫자 갯수 확인
    counted_number = collections.Counter(number)
    max_cnt = max(counted_number.values())

    # 조건 분기
    if same_color and same_number:
        return 900 + max(number)
    
    elif max_cnt == 4:
        for key, value in counted_number.items():
            if value == 4:
                return 800 + key
            
    elif max_cnt == 3 and len(counted_number) == 2:
        num_3, num_2 = 0, 0
        for key, value in counted_number.items():
            if value == 3:
                num_3 = key
            elif value == 2:
                num_2 = key
        return 700 + (10 * num_3) + num_2
    
    elif same_color:
        return 600 + max(number)
    
    elif same_number:
        return 500 + max(number)
    
    elif max_cnt == 3:
        num_3 = 0
        for key, value in counted_number.items():
            if value == 3:
                num_3 = key
                break
        return 400 + num_3
    
    elif len(counted_number) == 3:
        num_2_list = []
        for key, value in counted_number.items():
            if value == 2:
                num_2_list.append(key)
        return 300 + (max(num_2_list) * 10) + min(num_2_list)
    
    elif len(counted_number) == 4:
        for key, value in counted_number.items():
            if value == 2:
                return 200 + key

    return 100 + max(number)

def main():
    # 입력값
    deck = [tuple(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(5)]
    print(solve(deck))

if __name__ == "__main__":
    main()