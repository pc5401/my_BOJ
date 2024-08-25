import sys
input = sys.stdin.readline

def getDigit(k):
    n = 2
    v = n
    for i in range(1, 65):
        if k <= v:
            return (v-n, i)
        n *= 2
        v += n
    return i


def solve(k: int) -> int:
    v, n = getDigit(k)
    num = ['4'] * n
    binV = str(bin(k-v-1))[::-1]

    for i, b in enumerate(binV[:-2]):
        if b == 'b':
            break
        
        if b == '1':
            num[i] = '7'

        

    return "".join(num[::-1])


def main():
    # 입력값
    k = int(input())
    
    # 풀이
    result = solve(k)

    # 출력
    print(result)


if __name__ == "__main__":
    main()