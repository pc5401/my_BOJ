import sys
input = sys.stdin.readline
import collections

def race(N:int, lst: list) -> int:
    cnt_lst = collections.Counter(lst)
    team = set()
    team_score = collections.defaultdict(list)

    i = 0
    for v in lst:
        if cnt_lst[v] < 6:
            continue
        i += 1
        team_score[v].append(i)
        team.add(v)

    res, min_score = 0, 1e9
    
    for t in team:
        arr = team_score[t]
        s = sum(arr[:4])

        if s < min_score:
            res = t
            min_score = s

        elif s == min_score:
            if arr[4] < team_score[res][4]:
                res = t

    return res


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        print(race(int(input()), list(map(int,input().split()))))
