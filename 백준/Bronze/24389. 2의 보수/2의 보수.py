if __name__ == '__main__':
    N = int(input()) & 0xFFFFFFFF
    M = (~N + 1) & 0xFFFFFFFF
    print(bin(N ^ M).count('1'))