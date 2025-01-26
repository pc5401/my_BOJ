import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        lt, wt, le, we = map(int, input().split())
        area_t = lt * wt
        area_e = le * we
        if area_t > area_e:
            print("TelecomParisTech")
        elif area_t < area_e:
            print("Eurecom")
        else:
            print("Tie")

def main():
    solve()

if __name__ == "__main__":
    main()
