import sys
input = sys.stdin.readline

def is_matching(number, query, strike, ball):
    s = 0
    for i in range(3):
        if number[i] == query[i]:
            s += 1
    b_ = 0
    for i in range(3):
        for j in range(3):
            if i != j and number[i] == query[j]:
                b_ += 1
    return s == strike and b_ == ball

def solve(N, data):
    count_valid = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if j == i:
                continue
            for k in range(1, 10):
                if k == i or k == j:
                    continue
                number = str(i) + str(j) + str(k)
                flag = True
                for query, s, b in data:
                    if not is_matching(number, query, int(s), int(b)):
                        flag = False
                        break
                if flag:
                    count_valid += 1
    return count_valid

def main():
    N = int(input())
    data = []
    for _ in range(N):
        guess, s, b = input().split()
        data.append((guess, s, b))
    print(solve(N, data))

if __name__ == "__main__":
    main()
