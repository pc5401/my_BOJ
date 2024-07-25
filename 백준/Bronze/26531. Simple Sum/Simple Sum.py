def main():
    A = input()
    a, B = A.split('+')
    b, c = B.split('=')
    print('YES' if (int(a) + int(b)) == int(c) else 'NO')

main()