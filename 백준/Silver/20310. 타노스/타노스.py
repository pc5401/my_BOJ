import sys
input = sys.stdin.readline


if __name__ == '__main__':
    S = input().rstrip()
    one, zero = 0, 0 
    for s in S:
        if s == '1':
            one += 1
        else:
            zero += 1
    
    one_cnt, zero_cnt = one // 2, zero // 2
    n = one + zero
    lst = [ 1 if S[i] == '1' else 0 for i in range(n)]
    
    for i in range(n):
        if S[i] == '1' and one_cnt:
            lst[i] = 0
            one_cnt -= 1
        elif S[i] == '0' and zero_cnt:
            lst[i] = 1
            zero_cnt -= 1
        elif not one and not zero:
            break

    res_lst = [ S[i] for i in range(n) if lst[i]]

    print("".join(res_lst))