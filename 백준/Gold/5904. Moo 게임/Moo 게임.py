import sys
input = sys.stdin.readline

def moo(n:int, mo:int, value:int) -> str:
    # print(f'n:{n}, mo:{mo}, value:{value}')

    if n <= 3:
        return 'm' if n == 1 else 'o' 
    
    v = (value - mo) // 2
    
    if n <= v: # 앞
        return moo(n, mo-1, v)
    elif n <= v+mo: # 가운데
        return 'm' if n - v == 1 else 'o'
    else: # 뒤 부분
        return moo(n - v - mo, mo-1, v)


if __name__ == '__main__':
    N = int(input())
    mo, v = 3, 3
    while True:
        if N <= v:
            break
        mo += 1
        v = 2*v + mo
    print(moo(N, mo, v))