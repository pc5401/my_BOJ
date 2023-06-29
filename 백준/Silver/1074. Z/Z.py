def go_Z(n: int, r: int, c: int, k: int) -> int:
    if r == 0 and c == 0:
        return k
    v = 2**(n-1) 
    if r < v and c < v: # 1사분면
        return go_Z(n-1, r, c, k)
    elif r < v and c >= v: # 2사분면
        return go_Z(n-1, r, c-v, k+(v*v))
    elif r >= v and c < v: # 3사분면
        return go_Z(n-1,r-v,c,k+(v*v*2))
    else: # 4사분면
        return go_Z(n-1,r-v,c-v,k+(v*v*3))


if __name__ == '__main__':
    N, R, C = map(int,input().split())
    print(go_Z(N,R,C,0))
