import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    roads = list(map(int,input().split()))
    oils = list(map(int,input().split()))

    dp = [0] * N
    min_oil = oils[0]
    price = min_oil * roads[0]

    for i in range(1,N-1):
        if min_oil > oils[i]:
            min_oil = oils[i]
        price += min_oil * roads[i]

    print(price)