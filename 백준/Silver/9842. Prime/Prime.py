import sys
input = sys.stdin.readline

def solve(a: int) -> int:
    n = [1] * 104730
    n[0], n[1] = 0, 0

    cnt = 0

    for i in range(104730):
        if n[i]:
            cnt += 1
            for j in range(i, 104730, i):
                n[j] = 0
        
        if cnt == a:
            return i

    return -1


def main():
    # 입력
    a = int(input())
    
    # 풀이
    result = solve(a)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
