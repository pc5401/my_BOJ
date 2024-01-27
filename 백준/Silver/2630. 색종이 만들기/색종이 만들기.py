import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    white, blue = 0, 0

    def cut(r1, c1, r2, c2):
        global white, blue
        
        if all( v== 1 for ppr in paper[r1:r2] for v in ppr[c1:c2]):
            blue += 1
            return
        
        elif all( v== 0 for ppr in paper[r1:r2] for v in ppr[c1:c2]):
            white += 1
            return
        
        mid_r, mid_c = (r1 + r2) // 2, (c1 + c2) // 2

        cut(r1, c1, mid_r, mid_c)
        cut(r1, mid_c, mid_r, c2)
        cut(mid_r, c1, r2, mid_c)
        cut(mid_r, mid_c, r2, c2)

    cut(0, 0, N, N)
    print(white)
    print(blue)