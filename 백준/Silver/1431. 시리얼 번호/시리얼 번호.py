import sys
input = sys.stdin.readline



def sort_algo(X: str):
    lst = []
    for x in X:
        if x.isdigit():
            lst.append(x)

    return sum(map(int, lst))


def main():
    # 입력값
    N = int(input())
    lst = [input().rstrip() for _ in range(N)]

    result = sorted(lst, key=lambda x : (len(x), sort_algo(x), x))
    for res in result:
        print(res)

if __name__ == "__main__":
    main()