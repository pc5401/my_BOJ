import sys
import collections
input = sys.stdin.readline

def A(s: tuple[int]) -> tuple[int]:
    return (s[7], s[6], s[5], s[4],
            s[3], s[2], s[1], s[0])

def B(s: tuple[int]) -> tuple[int]:
    return (s[3], s[0], s[1], s[2],
            s[5], s[6], s[7], s[4])


def C(s: tuple[int]) -> tuple[int]:
    return (s[0], s[2], s[5], s[3],
            s[4], s[6], s[1], s[7])


def D(s: tuple[int]) -> tuple[int]:
    return (s[4], s[1], s[2], s[3],
            s[0], s[5], s[6], s[7])


def solve(target: tuple[int]) -> int:
    init = (1,2,3,4,5,6,7,8)
    dist = {init: 0}
    Q = collections.deque([init])

    while Q:
        s = Q.popleft()
        d = dist[s]

        for func in (A, B, C, D):
            t = func(s)
            if t not in dist:
                dist[t] = d + 1
                Q.append(t)

    return dist[target]


def main():
    # 입력
    target = tuple(map(int, input().split()))

    # 풀이
    result = solve(target)

    # 출력
    print(result)

if __name__ == "__main__":
    main()