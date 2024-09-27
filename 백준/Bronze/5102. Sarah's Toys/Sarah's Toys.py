import sys
input = sys.stdin.readline

def main():
    while True:
        line = input().strip()
        if not line:
            continue
        N_str, M_str = line.split()
        N, M = int(N_str), int(M_str)
        if N == 0 and M == 0:
            break
        T = N - M  # 방에 있는 장난감의 수
        if T >= 2:
            if T % 2 == 0:
                pairs = T // 2
                group_of_3 = 0
            else:
                pairs = (T - 3) // 2
                group_of_3 = 1
        else:
            pairs = 0
            group_of_3 = 0
        print(f"{pairs} {group_of_3}")

if __name__ == "__main__":
    main()
