import sys
input = sys.stdin.readline


def who_is_winning(a: int, b: int) -> int:
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return 2


def cal_time(time_goal: list[str]) -> str:
    minute = 0
    second = 0
    n = len(time_goal)

    for i in range(0, n, 2):
        start_m, start_s = map(int, time_goal[i].split(':'))
        end_m, end_s = map(int, time_goal[i+1].split(':'))
        minute += (end_m - start_m)
        second += (end_s - start_s)

    minute += (second // 60)
    second = second % 60
    if second < 0:
        minute -= 1
        second += 60
    
    rtn_m = str(minute) if minute > 9 else '0'+ str(minute)
    rtn_s = str(second) if second > 9 else '0' + str(second)

    return f'{rtn_m}:{rtn_s}'


def solve(N: int, team_times: list[tuple[int]]) -> tuple[int]:
    score_1, score_2 = 0, 0
    
    time_1_goal = []
    time_2_goal = []
    win = 0
    for team, time in team_times:
        if team == '1':
            score_1 += 1
        else:
            score_2 += 1
        
        curr = who_is_winning(score_1, score_2)
        
        if (win == 1 and curr == 0) or (win == 0 and curr == 1):
            time_1_goal.append(time)
        elif (win == 2 and curr == 0) or (win == 0 and curr == 2):
            time_2_goal.append(time)
        win = curr
    
    if win == 1:
        time_1_goal.append('48:00')
    elif win == 2:
        time_2_goal.append('48:00')

    team_win_time_1 = cal_time(time_1_goal) if time_1_goal else '00:00'
    team_win_time_2 = cal_time(time_2_goal) if time_2_goal else '00:00'

    return team_win_time_1, team_win_time_2


def main():
    # 입력값
    N = int(input())
    team_times: list[tuple[str]] = [tuple(input().split()) for _ in range(N)]

    # 풀이
    result: tuple[str] = solve(N, team_times)
    
    # 출력
    print(result[0])
    print(result[1])

    
if __name__ == "__main__":
    main()

    