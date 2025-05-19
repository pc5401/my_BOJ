import sys
input = sys.stdin.readline

def solve(triples):
    total = right = acute = obtuse = 0
    for a, b, c in triples:
        x, y, z = sorted((a, b, c))
        if x + y <= z:
            break
        total += 1
        s = x*x + y*y
        if s == z*z:
            right += 1
        elif s > z*z:
            acute += 1
        else:
            obtuse += 1
    return total, right, acute, obtuse

def main():
    # 입력
    triples = []
    for line in sys.stdin:
        a, b, c = map(int, line.split())
        triples.append((a, b, c))
    # 풀이
    total, right, acute, obtuse = solve(triples)
    # 출력
    print(total, right, acute, obtuse)

if __name__ == "__main__":
    main()
