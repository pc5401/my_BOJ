import sys
import collections
input = sys.stdin.readline


def solve(N: int, prerequisite_cnt: list[int], prerequisite_data: collections.defaultdict) -> list[int]:
    rtn = [0] * N

    Q = collections.deque()
    for i in range(1, N+1):
        if prerequisite_cnt[i] == 0:
            rtn[i-1] = 1
            Q.append(i)

    while Q:
        lecture = Q.popleft()

        for i in prerequisite_data[lecture]:
            prerequisite_cnt[i] -= 1
            if prerequisite_cnt[i] == 0:
                Q.append(i)
                rtn[i-1] = rtn[lecture-1] + 1

    return rtn


if __name__ == "__main__":
    # 입력값
    N, M = map(int, input().split())
    prerequisite_cnt = [0] * (N+1)
    prerequisite_data = collections.defaultdict(list)

    for _ in range(M):
        A, B = map(int, input().split())
        prerequisite_cnt[B] += 1
        prerequisite_data[A].append(B)

    # 풀이
    result = solve(N, prerequisite_cnt, prerequisite_data)

    # 출력
    print(*result)
