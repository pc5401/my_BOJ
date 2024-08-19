import sys
input = sys.stdin.readline

def getFourth(fst: str, snd: str, trd: str) -> int:
    if fst.isdigit():
        return int(fst) + 3
    elif snd.isdigit():
        return int(snd) + 2
    elif trd.isdigit:
        return int(trd) + 1
    

def solve(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    return str(n)


def main():
    fst = input().rstrip()
    snd = input().rstrip()
    trd = input().rstrip()

    print(solve(getFourth(fst, snd, trd)))


main()