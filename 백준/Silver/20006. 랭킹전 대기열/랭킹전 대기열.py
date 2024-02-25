import sys
input = sys.stdin.readline

def what_room_number(level: int, rooms: list) -> int:
    global m
    
    for number, room in enumerate(rooms):
        if len(room) >= m:
            continue

        if room[0][0] - 10 <= level <= room[0][0] + 10:
            return number

    return -1


if __name__ == '__main__':
    p, m = map(int, input().split())
    players = [tuple(map(lambda x : int(x) if x.isdecimal() else x, input().split())) for _ in range(p)]
    rooms = []
    
    for level, player in players:
        room_number = what_room_number(level, rooms)
        if room_number == -1:
            rooms.append([(level, player)])
        else:
            rooms[room_number].append((level, player))
    
    for room in rooms:
        sorted_room = sorted(room, key=lambda x : x[1])
        
        print('Waiting!') if len(room) < m else print('Started!')
        
        for level, player in sorted_room:
            print(level, player)