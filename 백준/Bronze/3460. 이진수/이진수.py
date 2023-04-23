import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        n = int(input())
        b = str(bin(n))
        lst = []
        for i,v in enumerate(b[::-1]):
            if v == '1':
                lst.append(i)
        print(*lst)