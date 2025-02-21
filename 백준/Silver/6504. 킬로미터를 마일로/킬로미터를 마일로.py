import sys
input = sys.stdin.readline

def solve(t: int, km_lst: list[int]) -> list[int]:
    fibo = [1, 2]
    while fibo[-1] <= 25000:
        fibo.append(fibo[-1] + fibo[-2])

    result = []
    for orig_x in km_lst:
        x = orig_x
        rep = ""
        flag = False 
        for num in reversed(fibo):
            if num <= x:
                rep += "1"
                x -= num
                flag = True
            else:
                if flag:
                    rep += "0"

        if len(rep) <= 1:
            result.append(0)
        else:
            rep_shifted = rep[:-1] 
            rep_rev = rep_shifted[::-1]
            y = 0
            for i, ch in enumerate(rep_rev):
                if ch == '1':
                    y += fibo[i]
            result.append(y)
    return result

def main():
    # 입력
    t = int(input())
    km_lst = [int(input()) for _ in range(t)]
    
    # 풀이
    result = solve(t, km_lst)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()