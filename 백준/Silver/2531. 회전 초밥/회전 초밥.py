import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값
    N, d, k, c = map(int, input().split())
    line = [int(input()) for _ in range(N)]
    # 초기화
    foods = {i:0 for i in range(1,d+1)}
    foods[c] = 1
    res = 1
    
    for i in range(k):
        if not foods[line[i]]:
            foods[line[i]] += 1
            res += 1
        else:
            foods[line[i]] += 1

    val = res
    for i in range(N):
        foods[line[i]] -= 1
        if not foods[line[i]]:
            val -= 1
        
        j = (i+k) % N
        if not foods[line[j]]:
            val += 1
        foods[line[j]] += 1

        res = max(res, val)

    print(res)