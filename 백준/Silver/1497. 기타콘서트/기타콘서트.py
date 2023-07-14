import sys
import itertools
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력과 전처리
    N, M = map(int,input().split())
    lst = [0] * N
    for i in range(N):
        word, num = input().split()
        num = num.replace('Y', '1')
        num = num.replace('N', '0')
        lst[i] = int(num,2)
    res, maxV = -1, 0
    value = 2**M -1
    idx = 1

    while idx <= N:
        for c in itertools.combinations(range(N), idx):
            v = lst[c[0]]
            for i in c[1:]:
                v |= lst[i]
            
            cnt = 0
            while v:
                cnt += (v & 1)
                v = v >> 1

            if cnt > maxV:
                res = idx
                maxV = cnt

        idx +=1

    print(res)