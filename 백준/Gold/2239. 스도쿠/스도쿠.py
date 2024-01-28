import sys
input = sys.stdin.readline

def possible_nums(x: int, y: int, doku:list) -> list:
    if doku[x][y] > 0:
        return []
    a = set()
    b = {n for n in range(1, 10)}
    for i in range(9):
        a.add(doku[x][i])
        a.add(doku[i][y])

    xlst = [0,1,2] if x < 3 else [3,4,5] if x < 6 else [6,7,8]
    ylst = [0,1,2] if y < 3 else [3,4,5] if y < 6 else [6,7,8]

    for i in xlst:
        for j in ylst:
            a.add(doku[i][j])

    return list(b - a)

def dfs(idx: int,data: list, data_keys:list, doku:list):
    if len(data_keys) == idx:
        return 1
    
    key = data_keys[idx]
    x, y = key
    xlst = [0,1,2] if x < 3 else [3,4,5] if x < 6 else [6,7,8]
    ylst = [0,1,2] if y < 3 else [3,4,5] if y < 6 else [6,7,8]
    
    for n in data[key]:
        if n in doku[x]:
            continue
        if n in [doku[i][y] for i in range(9)]:
            continue
        if any(doku[i][j] == n for i in xlst for j in ylst):
            continue

        doku[x][y] = n
        if dfs(idx+1,data, data_keys, doku):
            return 1
        doku[x][y] = 0




def dfs_setting(nums, doku):

    data = dict()
    for i in range(9):
        for j in range(9):
            if doku[i][j] == 0:
                data[(i,j)] = nums[i][j]
    
    data_keys = [*data.keys()]

    for idx, key in enumerate(data_keys):
        x, y = key
        for n in data[key]:
            doku[x][y] = n
            if dfs(idx+1,data, data_keys, doku):
                return 
            doku[x][y] = 0



if __name__ == '__main__':
    doku = [[int(char) for char in input().rstrip()] for _ in range(9)]
    nums = [[possible_nums(i, j, doku) for j in range(9)]for i in range(9)]
    
    while True:

        flag = 0

        for i in range(9):
            for j in range(9):
                if len(nums[i][j]) == 1:
                    doku[i][j] = nums[i][j].pop()
                    flag = 1
        if not flag:
            break
        nums = [[possible_nums(i, j, doku) for j in range(9)]for i in range(9)]
    
    if  any(nums[i][j] for i in range(9) for j in range(9)):
        dfs_setting(nums, doku)
    
    for res in doku:
        print("".join(map(str, res)))