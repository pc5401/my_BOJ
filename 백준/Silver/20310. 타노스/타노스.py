import sys
input = sys.stdin.readline

if __name__ == '__main__':
    S = input().rstrip()
    one, zero = 0, 0 
    for s in S:
        if s == '1':
            one += 1
        else:
            zero += 1
    
    print('0'*(zero//2) + '1'*(one//2))