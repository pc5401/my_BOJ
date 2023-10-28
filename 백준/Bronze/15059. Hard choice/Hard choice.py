if __name__ == "__main__":
    Ca, Ba, Pa = map(int, input().split())
    Cr, Br, Pr = map(int, input().split())
    C = Cr - Ca
    B = Br - Ba
    P = Pr - Pa
    res = 0
    for v in (C, B, P):
        if v > 0:
            res += v
    print(res)