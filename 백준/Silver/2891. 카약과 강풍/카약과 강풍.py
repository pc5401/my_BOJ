import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, S, R = map(int, input().split())
    broken_team = list(map(int, input().split()))
    spare_team = list(map(int, input().split()))
    give_spare = []
    team = [0] * N
    
    broken_team.sort()
    spare_team.sort()
    
    for num in broken_team:
        team[num-1] = 1

    for num in spare_team:
        if team[num-1]:
            team[num-1] = 0
        else:
            give_spare.append(num)

    for num in give_spare:

        if 1 < num and team[num-2]:
            team[num-2] = 0
        elif num < N and team[num]:
            team[num] = 0
    
    print(sum(team))


