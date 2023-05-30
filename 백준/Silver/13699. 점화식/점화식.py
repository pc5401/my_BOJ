if __name__ == "__main__":
    N = int(input())
    t = [0] * 36
    t[0], t[1], t[2], t[3] = 1, 1, 2, 5
    for i in range(4,36):
        for j in range(i):
            t[i] += t[j] * t[i-j-1]
    print(t[N])