import sys
input = sys.stdin.readline

def solve(A: int) -> int:
    # A의 소인수분해
    def factor(n: int) -> dict[int,int]:
        fs = {}
        d = 2
        while d * d <= n:
            if n % d == 0:
                cnt = 0
                while n % d == 0:
                    n //= d
                    cnt += 1
                fs[d] = cnt
            d += 1 if d == 2 else 2
        if n > 1:
            fs[n] = 1
        return fs

    fs = factor(A)
    # A^2 의 지수 리스트
    pals = [(p, e*2) for p, e in fs.items()]
    divs = [1]
    for p, e in pals:
        tmp = []
        for d in divs:
            v = 1
            for _ in range(e):
                v *= p
                tmp.append(d * v)
        divs += tmp

    A2 = A * A
    cnt = 0
    for d1 in divs:
        if d1 >= A:
            continue
        d2 = A2 // d1

        if (d1 ^ d2) & 1:
            continue
            
        B = (d2 - d1) // 2
        if B > A:
            cnt += 1
    return cnt

def main():
    # 입력
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        A = int(line)
        if A == 0:
            break
        # 풀이
        result = solve(A)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
