import sys
input = sys.stdin.readline

def solve(N: int, student_masks: list[int]) -> int:
    M = len(student_masks)
    full = (1 << N) - 1
    best = M+1
    # 모두 확인
    for mask in range(1 << M):
        covered = 0
        cnt = 0
        for i in range(M):
            if mask & (1 << i):
                covered |= student_masks[i]
                cnt += 1
        if covered == full:
            if cnt < best:
                best = cnt
    return best if best <= M else -1

def main():
    # 입력
    N, M = map(int, input().split())
    student_masks = []
    for _ in range(M):
        data = list(map(int, input().split()))
        oi, probs = data[0], data[1:]
        mask = 0
        for p in probs:
            mask |= 1 << (p-1)
        student_masks.append(mask)
    # 풀이
    result = solve(N, student_masks)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
