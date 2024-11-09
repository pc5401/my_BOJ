import sys
input = sys.stdin.readline

def main():
    # 입력값
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    
    # 풀이
    result = sorted(lst)
    
    # 출력 
    for res in result:
        print(res)

if __name__ == '__main__':
    main()
