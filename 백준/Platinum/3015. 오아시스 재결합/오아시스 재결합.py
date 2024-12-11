import sys
input = sys.stdin.readline

def solve(N: int, K: list[int]) -> int:
    rtn = 0
    stack = []

    for k in K:
        cnt = 1  
        while stack and stack[-1][0] < k:
            rtn += stack.pop()[1]
        
        if stack and stack[-1][0] == k:
            cnt = stack[-1][1] + 1
            rtn += stack[-1][1]
            stack.pop()
            if stack:
                rtn += 1  
        elif stack:
            rtn += 1 
        
        stack.append((k, cnt))
    
    return rtn
    
def main():
    # 입력값
    N = int(input())
    K = [int(input()) for _ in range(N)]

    # 풀이
    result = solve(N, K)
    
    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()