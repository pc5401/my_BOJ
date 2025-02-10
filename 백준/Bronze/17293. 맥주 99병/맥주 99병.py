import sys
input = sys.stdin.readline

def solve(k: int, n: int):
    if k > 2:
        return f'{k} bottles of beer on the wall, {k} bottles of beer.\nTake one down and pass it around, {k-1} bottles of beer on the wall.'
    elif k == 2:
        return '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.'
    elif k == 1:
        return '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.'
    else:
        if n == 1:
            return 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 1 bottle of beer on the wall.'
        else:
            return f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {n} bottles of beer on the wall.'

    

def main():
    # 입력
    N = int(input())

    # 풀이
    result = [solve(i, N) for i in range(N, -1, -1)]

    # 출력
    for res in result:
        print(res)
        print()

if __name__ == "__main__":
    main()