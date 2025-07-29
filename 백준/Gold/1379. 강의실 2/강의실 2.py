import sys
import heapq
input = sys.stdin.readline

def solve(n: int, lectures: list[tuple[int, int, int]]) -> tuple[int, list[int]]:
    lectures.sort(key=lambda x: x[1])
    
    # 우선순위 큐 => 강의 종료 시간, 강의실 번호
    pq = []
    room_assign = [0] * (n + 1)
    room_count = 0

    for idx, start, end in lectures:
        if pq and pq[0][0] <= start:
            finish_time, room_num = heapq.heappop(pq)
        else:
            room_count += 1
            room_num = room_count

        room_assign[idx] = room_num
        heapq.heappush(pq, (end, room_num))
    
    return room_count, room_assign[1:]

def main():
    # 입력
    n = int(input())
    lectures = [tuple(map(int, input().split())) for _ in range(n)]

    # 풀이
    room_count, assignments = solve(n, lectures)

    # 출력
    print(room_count)
    print('\n'.join(map(str, assignments)))

if __name__ == "__main__":
    main()
