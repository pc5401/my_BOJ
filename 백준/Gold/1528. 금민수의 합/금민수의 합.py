import sys
import collections
input = sys.stdin.readline

def get_number(length: int) -> list[int]:
    if length >= 7:
        length = 6
    rtn = []

    for bitmask in range(1 << length):
        num_str = ""
        # 각 비트를 확인하며 0이면 '4', 1이면 '7'
        for j in range(length):
            if bitmask & (1 << j):
                num_str = "7" + num_str
            else:
                num_str = "4" + num_str
        rtn.append(int(num_str))

    return rtn

def backtrack(N, predecessor, choice):
    if predecessor[N] == -1:
        return [-1]

    result = []
    cur = N
    while cur != 0:
        result.append(choice[cur])
        cur = predecessor[cur]

    result.reverse()
    return result


def solve(n: int, numbers: list[int]) -> int:
    predecessor = [-1] * (n+1)
    choice = [-1] * (n+1)
    visited = [False] * (n+1)

    Q = collections.deque()
    
    Q.append(0)
    visited[0] = True
    
    while Q:
        curr_val = Q.popleft()

        for num in numbers:
            next_val = curr_val + num
            if next_val > n:
                break

            if not visited[next_val]:
                visited[next_val] = True
                predecessor[next_val] = curr_val
                choice[next_val] = num
                Q.append(next_val)

                if next_val == n:
                    return backtrack(n, predecessor, choice)

    return [-1]


if __name__=="__main__":
    # 입력
    N = input().rstrip()

    # 풀이
    numbers = []
    for i in range(1, len(N)+1):
        numbers.extend(get_number(i))
    result = solve(int(N), numbers)
    
    # 출력
    print(*result)