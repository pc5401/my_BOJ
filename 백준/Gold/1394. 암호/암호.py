import sys
input = sys.stdin.readline

MOD = 900528

def solve(keys: str, ps: str) -> int:
    n: int = len(keys)
    m: int = len(ps)

    keyboard = {key: idx + 1 for idx, key in enumerate(keys)}
    
    rtn = 0
    num = 1
    for word in ps[::-1]:
        rtn = (rtn + keyboard[word] * num) % MOD
        num = (num * n) % MOD
    
    return rtn % 900528

def main():
    # 입력값
    keys: str = input().rstrip()
    ps: str = input().rstrip()

    # 풀이
    result: int = solve(keys, ps)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()

