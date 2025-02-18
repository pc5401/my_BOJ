import sys
input = sys.stdin.readline


def num_display(s: int, lst: list[str], code: str):
    delta = {'0' : ' ', '1' : '-'}
    for i in range(2*s + 3):
        if i == 0:
            lst[i] += (' ' + delta[code[0]] * s + ' ')
        elif i == s + 1:
            lst[i] += (' ' + delta[code[2]] * s + ' ')
        elif i == 2*s + 2:
            lst[i] += (' ' + delta[code[4]] * s + ' ')
        
        elif i <= s:
            if code[1] == 'b':
                lst[i] += ('|' + (' ' * (s+1) ))
            elif code[1] == 'd':
                lst[i] += ((' '*(s+1) ) + '|')
            else:
                lst[i] += ('|' + ' '*(s) + '|')
        
        else:
            if code[3] == 'b':
                lst[i] += ('|' + (' ' * (s+1) ))
            elif code[3] == 'd':
                lst[i] += ((' ' * (s+1)) + '|')
            else:
                lst[i] += ('|' + ' '*(s) + '|')

        lst[i] += ' '



def solve(s: int, n: str) -> list[str]:
    data = {
    '1': '0d0d0',
    '2': '1d1b1',
    '3': '1d1d1',
    '4': '0m1d0',
    '5': '1b1d1',
    '6': '1b1m1',
    '7': '1d0d0',
    '8': '1m1m1',
    '9': '1m1d1',
    '0': '1m0m1'
    }

    rtn = [''] * (2*s+3)
    
    for i in n:
        num_display(s, rtn, data[i])
    
    return rtn


def main():
    # 입력
    s, n = input().split()

    # 풀이
    result = solve(int(s), n)
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
