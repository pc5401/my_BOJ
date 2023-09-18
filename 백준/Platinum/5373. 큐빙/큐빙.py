import sys
input = sys.stdin.readline


def determine_face(face:str ):
    if face == 'U':
        values = [[0, 1, 2], [2, 5, 8],[8, 7, 6],[6, 3, 0]]
        return [2, 4, 3, 5], values
    
    elif face == 'D':
        values = [[6, 7, 8], [0, 3, 6],[2, 1, 0],[8, 5, 2]]
        return [2, 4, 3, 5], values
    
    elif face == 'F':
        values = [[6, 7, 8], [6, 7, 8],[2, 1, 0],[6, 7, 8]]
        return [0, 5, 1, 4], values
    
    elif face == 'B':
        values = [[0, 1, 2], [0, 1, 2],[8, 7, 6],[0, 1, 2]]
        return [0, 5, 1, 4], values
    
    elif face == 'L':
        values = [[0, 3, 6], [0, 3, 6],[0, 3, 6],[0, 3, 6]]
        return [0, 2, 1, 3], values
    
    elif face == 'R':
        values = [[2, 5, 8], [2, 5, 8], [2, 5, 8],[2, 5, 8]]
        return [0, 2, 1, 3], values

def turn_main(face:str, dir:str, cube: list):
    temp = cube[face][:]
    if dir == '+': # 시계 방향
        cube[face][0], cube[face][1], cube[face][2], = temp[6], temp[3], temp[0]
        cube[face][3], cube[face][4], cube[face][5], = temp[7], temp[4], temp[1]
        cube[face][6], cube[face][7], cube[face][8], = temp[8], temp[5], temp[2]
    else:
        cube[face][0], cube[face][1], cube[face][2] = temp[2], temp[5], temp[8]
        cube[face][3], cube[face][4], cube[face][5] = temp[1], temp[4], temp[7]
        cube[face][6], cube[face][7], cube[face][8] = temp[0], temp[3], temp[6]  
        


def turn_face(face:str, dir:str, cube: list, faces: list, values:list):
    if (dir == '+' and face in ('U', 'F', 'L')) or (dir == '-' and face in ('D', 'B', 'R')):
        # 정방향
        now_cube = [ cube[faces[3]][k] for k in values[3]]
        for i in range(4):
            next_cube = [ cube[faces[i]][k] for k in values[i]]
            for j in range(3):
                cube[faces[i]][values[i][j]] = now_cube[j]
            now_cube = next_cube
    else:
        # 역방향
        now_cube = [ cube[faces[0]][k] for k in values[0]]
        for i in range(3,-1,-1):
            next_cube = [ cube[faces[i]][k] for k in values[i]]
            for j in range(3):
                cube[faces[i]][values[i][j]] = now_cube[j]
            now_cube = next_cube


if __name__ == "__main__":
    # 입력 & 전처리
    num_color = {1: 'w', 2 :'y', 3 :'r', 4: 'o', 5: 'g', 6 : 'b'}
    face_num = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
    
    T = int(input())
    for tc in range(T):
        cube = [[i]*9 for i in range(1, 7)]
        N = int(input())
        input_lst = list(input().split())
        cnt = 1
        for word in input_lst:
            word, clock_dir = word[0], word[1]
            faces, values = determine_face(word) # 4개
            turn_face(word, clock_dir, cube, faces, values)
            turn_main(face_num[word],clock_dir, cube) # 정면 돌리기'
        
        # 출력
        top = cube[0]
        print(num_color[top[0]] + num_color[top[1]] + num_color[top[2]])
        print(num_color[top[3]] + num_color[top[4]] + num_color[top[5]])
        print(num_color[top[6]] + num_color[top[7]] + num_color[top[8]])