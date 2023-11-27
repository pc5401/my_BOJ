import sys
input = sys.stdin.readline


if __name__ == "__main__":
    player, game_round = map(int, input().split())
    game_score = list(map(int, input().split()))
    player_score = [0] * player
    for R in range(0,  game_round*player, player):
        for P in range(player):
            player_score[P] += game_score[R+P]
    
    res = 0
    maxV = 0
    for num, score in enumerate(player_score):
        if maxV <= score:
            maxV = score
            res = (num+1)

    print(res)  
