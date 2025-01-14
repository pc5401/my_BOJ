import sys
input = sys.stdin.readline


def get_number(length: int) -> list[int]:
    rtn = []

    for bitmask in range(1 << length):
        num_str = ""
        # 각 비트를 확인하며 0이면 '4', 1이면 '7'
        for j in range(length):
            if bitmask & (1 << j):
                num_str = "7" + num_str
            else:
                num_str = "4" + num_str
        rtn.append(int(num_str))
    
    return rtn


def solve(A: int, B: int) -> int:
    
    lenA = len(str(A))
    lenB = len(str(B))
    rtn = 0
    for length in range(lenA, lenB+1):
        numbers = get_number(length)
        for num in numbers:
            if num > B:
                break
            if num >= A:
                rtn += 1
    
    return rtn



if __name__=="__main__":
    # 입력
    A, B = map(int, input().split())

    # 풀이
    result = solve(A, B)
    
    # 출력
    print(result)
