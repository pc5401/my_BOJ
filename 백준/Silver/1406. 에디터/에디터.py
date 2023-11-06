import sys
input = sys.stdin.readline


if __name__ == "__main__":
    left = list(input().rstrip())
    M = int(input())
    orders = [tuple(input().split()) for _ in range(M)]
    right = []

    for order in orders:
        if order[0] == 'L' and left:
            right.append(left.pop())
        elif order[0] == 'D' and right:
            left.append(right.pop())
        elif order[0] == 'B' and left:
            left.pop()
        elif order[0] == 'P':
            left.append(order[1])
    
    print("".join(left) + "".join(right[::-1]))



