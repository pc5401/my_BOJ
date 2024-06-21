import sys
input = sys.stdin.readline


def solve(N: int, numbers: list[int]) -> int:
    data = set()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == N:
                x = min(numbers[i], numbers[j])
                y = max(numbers[i], numbers[j])
                data.add((x,y))
    
    rtn = list(data)
    rtn.sort(key=lambda x : (x[0], x[1]))
    return rtn


def main():
    # 입력값
    numbers = list(map(int, input().split())) 
    N = int(input())
    # 풀이
    result: int= solve(N, numbers)

    # 출력
    for res in result:
        print(*res)
    print(len(result))

if __name__ == "__main__":
    main()