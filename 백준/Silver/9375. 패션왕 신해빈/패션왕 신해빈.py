import sys
input = sys.stdin.readline


def solve(n: int, lst: list[list[str]]) -> int:
    rtn = 1
    costume_set = dict()

    for cloth, category in lst:
        if costume_set.get(category):
            costume_set[category] += 1
        else:
            costume_set[category] = 1


    for costume in costume_set:
        rtn *= (costume_set[costume] + 1)

    return rtn - 1


def main():
    T = int(input())
    N_lst = []
    input_lst = []
    for tc in range(T):
        N = int(input())
        N_lst.append(N)
        input_lst.append([input().split() for _ in range(N)])
    
    result = []
    for tc in range(T):
        result.append(solve(N_lst[tc], input_lst[tc]))
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
