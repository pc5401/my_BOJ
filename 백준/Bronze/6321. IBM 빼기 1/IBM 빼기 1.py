import sys
input = sys.stdin.readline

def shift_alphabet(s):
    result = ""
    for char in s:
        if char == 'Z':
            result += 'A'
        else:
            result += chr(ord(char) + 1)
    return result

if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        S = input().strip()
        res = shift_alphabet(S)
        
        print(f'String #{tc+1}')
        print(res)
        if tc != T-1:
            print()