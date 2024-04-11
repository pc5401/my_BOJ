import sys
input = sys.stdin.readline

def main():
    # 입력값
    N = int(input())
    
    # 결과 출력
    for i in range(1, N):
        print('*'*i)
    
    for j in range(N, 0, -1):
        print('*'*j)


if __name__ == "__main__":
    main()