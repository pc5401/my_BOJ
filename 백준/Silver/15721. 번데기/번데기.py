import sys
input = sys.stdin.readline

def get_lst(num: int) -> list[int]:
    rtn = [0, 1, 0, 1]
    zero = [0] * num
    one = [1] * num
    
    rtn.extend(zero)
    rtn.extend(one)

    return rtn


def solve(A: int, T: int, N: int) -> int:
    cnt = 0
    num = 2
    a = -1

    while cnt < T:
        lst = get_lst(num)
        num += 1

        for v in lst:
            a = (a+1) % A
            if v == N:
                cnt += 1
            
            if cnt == T:
                break
        
    return a
        

if __name__ == "__main__":
    # 입력값
    A = int(input())
    T = int(input())
    N = int(input())
    
    # 풀이
    result = solve(A, T, N)
    
    # 출력    
    print(result)