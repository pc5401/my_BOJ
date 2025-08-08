import sys
input = sys.stdin.readline

def make_min_num(digs):
    digs_sorted = sorted(digs)
    
    if digs_sorted[0] != 0:
        return int(''.join(str(d) for d in digs_sorted))

    for i, d in enumerate(digs_sorted):
        if d != 0:
            first = str(d)
            zeros = i
            rest = ''.join(str(x) for x in digs_sorted[i+1:])
            return int(first + '0'*zeros + rest)

    return 0

def solve(N, arr):
    best = float('inf')
    total_masks = 1 << N
    # 각 숫자에 인덱스 부여
    for mask in range(1, total_masks - 1):
        a_digits = []
        b_digits = []
        has_a_nz = False
        has_b_nz = False
        for i in range(N):
            if mask & (1 << i):
                a_digits.append(arr[i])
                if arr[i] != 0:
                    has_a_nz = True
            else:
                b_digits.append(arr[i])
                if arr[i] != 0:
                    has_b_nz = True
        if not (has_a_nz and has_b_nz):
            continue

        a_num = make_min_num(a_digits)
        b_num = make_min_num(b_digits)
        s = a_num + b_num
        if s < best:
            best = s

    return best

def main():
    while True:
        data = input().split()
        N = int(data[0])
        if N == 0:
            break
        arr = list(map(int, data[1:]))

        # 풀이
        result = solve(N, arr)

        # 출력
        print(result)

if __name__ == "__main__":
    main()
