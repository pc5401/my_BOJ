import sys
input = sys.stdin.readline

if __name__ == "__main__":
    data = 0
    a = (1 << 21)-1

    M = int(input())
    for _ in range(M):
        order = input().split()
        if order[0] == 'add': 
            data |= 1 << int(order[1])
        elif order[0] == 'remove':
            data &= ~(1 << int(order[1]))
        elif order[0] == 'check':
            if data & (1<<int(order[1])):
                print(1)
            else:
                print(0)

        elif order[0] == 'toggle':
            data ^= 1 << int(order[1])

        elif order[0] == 'all':
            data = (1 << 21)-1
        elif order[0] == 'empty':
            data = 0
