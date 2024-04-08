import sys
input = sys.stdin.readline


def solve(N, L, D):
    total_album_time = N*L + (N-1)*5
    
    bell_time = 0
    while bell_time <= total_album_time:
        if bell_time % (L+5) < L:
            bell_time += D
        else:
            break
    
    if bell_time <= total_album_time:
        return bell_time
    else:
        return total_album_time + D - (total_album_time % D)


def main():
    # 입력값
    N, L, D = map(int, input().split())
    print(solve(N, L, D))


if __name__ == "__main__":
    main()
