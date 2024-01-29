import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    xlst = list(map(int, input().split()))
    
    score = {x:0 for x in xlst}
    maxX = max(xlst)

    for x in xlst:
        for y in range(x+x, maxX+1, x):
            if y in score:
                score[x] += 1
                score[y] -= 1
    
    print(*[score[x] for x in xlst])