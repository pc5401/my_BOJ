if __name__ == "__main__":
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort() # 정렬
    end = 0.0
    cnt = 0
    for v in lst:
        if v > end:
            cnt += 1
            end = v + M - 0.5
    print(cnt)