import sys
input = sys.stdin.readline


def main():
    N = int(input())
    order_list = list(input().rstrip())

    xylograph = [[46]*N for _ in range(N)]
    delta = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}
    
    robot_arm = [0,0]
    for idx, order in enumerate(order_list):
        if order == 'D':
            xylograph[0][0] = 124
            break
        if order == 'R':
            xylograph[0][0] = 45
            break
    
    for order in order_list:

        dir = delta[order]
        ni, nj = robot_arm[0] + dir[0], robot_arm[1] + dir[1]
        if 0 <= ni < N and 0 <= nj < N:
            if xylograph[ni][nj] == 46:
                if order == 'D' or order == 'U':
                    xylograph[ni][nj] = 124
                else:
                    xylograph[ni][nj] = 45
            elif xylograph[ni][nj] == 45 and (order == 'D' or order == 'U'):
                xylograph[ni][nj] = 43
            elif xylograph[ni][nj] == 124 and (order == 'L' or order == 'R'):
                xylograph[ni][nj] = 43
            
            if xylograph[robot_arm[0]][robot_arm[1]] == 124 and (order == 'L' or order == 'R'):
                xylograph[robot_arm[0]][robot_arm[1]] = 43
            elif xylograph[robot_arm[0]][robot_arm[1]] == 45 and (order == 'D' or order == 'U'):
                xylograph[robot_arm[0]][robot_arm[1]] = 43
    
            robot_arm[0], robot_arm[1] = ni, nj
    
    result = [list(map(chr, x)) for x in xylograph]

    for res in result:
        print("".join(res))


if __name__ == "__main__":
    main()
