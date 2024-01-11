import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    result = []
    # 입력값 처리
    tc = int(input())
    for _ in range(tc):
        P = list(input().rstrip())
        N = int(input())
        lst = collections.deque(input().rstrip().replace('[', '').replace(']','').split(','))
        if not N:
            lst.pop()
        # 연산
        
        is_rev = False
        is_err = False
        for p in P:

            if p == 'R':
                is_rev = False if is_rev else True
            elif p == 'D' and lst:
                if is_rev:
                    lst.pop()
                else:
                    lst.popleft()
            elif p == 'D':
                is_err = True
                break
        # 결과 계산

        if is_err:
            result.append('error')
            continue

        if is_rev:
            temp = []
            while lst:
                temp.append(lst.pop())
            lst = temp

        res = '['
        if not lst:
            res += ']'
            result.append(res)
            continue
        
        for i, num in enumerate(lst):
            res += num
            if i == len(lst)-1:
                res += ']'
            else:
                res += ','

        result.append(res)
    # 결과 출력
    for res in result:
        print(res)
