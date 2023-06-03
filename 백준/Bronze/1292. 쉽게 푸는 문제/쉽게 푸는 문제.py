import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B = map(int,input().split())
    sum_lst = [0]
    for i in range(1, 50):
        for j in range(i):
            sum_lst.append(i)

    for i in range(1,1001):
        sum_lst[i] += sum_lst[i-1]
    print(sum_lst[B] - sum_lst[A-1])