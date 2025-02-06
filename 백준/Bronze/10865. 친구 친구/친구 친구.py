import sys
input = sys.stdin.readline

def main():
    # 입력값
    N, M = map(int, input().split())
    friends = [0] * (N+1)
    
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a] += 1
        friends[b] += 1
        

    # 출력
    for i in range(1, N+1):
        print(friends[i])

if __name__ == "__main__":
    main()
