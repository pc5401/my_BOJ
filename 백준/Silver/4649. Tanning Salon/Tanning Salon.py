import sys
input = sys.stdin.readline

def solve(beds, seq):
    occupied = 0
    tanned = set()
    left = set()
    walked = 0

    for c in seq:
        # 도착
        if c not in tanned and c not in left:
            if occupied < beds:
                occupied += 1
                tanned.add(c)
            else:
                walked += 1
                left.add(c)
        # 출발
        else:
            if c in tanned:
                occupied -= 1
                tanned.remove(c)

    return walked

def main():
    while True:
        # 입력
        data = input().split()
        beds = int(data[0])
        if beds == 0:
            break
        seq = data[1]

        # 풀이
        result = solve(beds, seq)

        # 출력
        if result == 0:
            print("All customers tanned successfully.")
        else:
            print(f"{result} customer(s) walked away.")

if __name__ == "__main__":
    main()
