import sys
input = sys.stdin.readline


def myRank(n: int, k: int, team_id: int, logs: list) -> int:
    score_board = [[0]*(k+2) for _ in range(n)]

    for time, log in enumerate(logs, start=1):
        id, num, score = log
        score_board[id-1][0] += 1 # 제출 횟수
        score_board[id-1][num] = max(score_board[id-1][num], score)
        score_board[id-1][-1] = time # 제출 시간

    score_data = [(sum(score_board[id][1:k+1]), score_board[id][0], score_board[id][-1], id) for id in range(n)]
    score_data.sort(key=lambda x:(-x[0], x[1], x[2]))
    
    for rank, val in enumerate(score_data, start=1):
        if val[3] == team_id:
            return rank

    return 0


if __name__ == '__main__':
    ranks = []
    T = int(input())
    for _ in range(T):
        n, k, team_id, m = map(int, input().split())
        logs = [list(map(int, input().split())) for _ in range(m)]
        ranks.append(myRank(n, k, team_id-1, logs))

    for rank in ranks:
        print(rank)
