import sys
input = sys.stdin.readline


def solve(N: int, lst: list[list[str]]) -> list[list[str]]:
    result = []
    data = dict()
    for mentor, mentee in lst:
        if not data.get(mentor):
            data[mentor] = [mentee]
        else:
            data[mentor].append(mentee)
    
    mentor_lst = sorted(data.keys())
    
    for mentor in mentor_lst:
        mentee_lst = sorted(data[mentor], reverse=True)
        for mentee in mentee_lst:
            result.append([mentor, mentee])
    
    return result
     

if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = [input().rstrip().split() for _ in range(N)]

    # 풀이
    result = solve(N, lst)

    # 출력
    for res in result:
        print(*res)