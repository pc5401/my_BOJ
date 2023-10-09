import sys
input = sys.stdin.readline


def solve(m: int, note: list, scale: list, number: list):
    rtn = []

    for sound in note:
        if len(sound) == 2:
            if sound[1] == 'b':
                n = number[sound[0]] - 1
            else:
                n = number[sound[0]] + 1
        else:
            n = number[sound]
        n = (n + m) % 12 
        rtn.append(scale[n])

    return rtn


if __name__ == "__main__":
    # 입력 & 전처리
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    number = {s : i for i,s in enumerate(scale)}
    res = []
    
    while True:
        note = list(input().split())
        if note[0] == '***':
            break
        m = int(input())
        res.append(solve(m, note, scale, number))

    
    for r in res:
        print(*r)