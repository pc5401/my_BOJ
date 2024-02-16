import sys
input = sys.stdin.readline


if __name__ == '__main__':
    games = {'Y':2,  'F':3, 'O':4}
    inputV = input().split()
    N, G = int(inputV[0]), games[inputV[1]]
    peoples = {input().rstrip() for _ in range(N)}
    print(len(peoples)//(G-1))