import sys
input = sys.stdin.readline


def first_idx_count(a_cnt: int) -> list:
    rtn = [0,0]
    for i in range(a_cnt):
        if word[i] == 'a':
            rtn[0] += 1
        else:
            rtn[1] += 1

    return rtn 

if __name__ == '__main__':
    # 입력값
    word = input().rstrip()

    # 초기화
    n = len(word)
    a_cnt =  word.count('a')
    ab = first_idx_count(a_cnt)
    res = ab[1]

    for i in range(n):
        if word[i] == 'a':
            ab[0] -= 1
        else:
            ab[1] -= 1

        if word[(i+a_cnt) % n] == 'a':
            ab[0] += 1
        else:
            ab[1] += 1

        res = min(res, ab[1])

    print(res)
