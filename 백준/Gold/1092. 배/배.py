import sys
input = sys.stdin.readline

def work(n, cranes, M, boxes):
    # 내림 차순
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    
    # 최대값 비교
    if cranes[0] < boxes[0]:
        return -1
    
    # 시간 초기화
    time = 0

    # 모든 박스를 배로 옮길 때까지 반복
    while boxes:
        #각 크레인에 대해 처리
        for crane in cranes:
            # 옮길 수 있는 박스를 찾기
            for i in range(len(boxes)):
                if crane >= boxes[i]:
                    # 해당 박스를 옮기고 목록 제거
                    del boxes[i]
                    break

        time += 1

    return time


if __name__ == "__main__":
    N = int(input())
    crane_lst = list(map(int, input().split()))
    M = int(input())
    box_lst = list(map(int, input().split()))
    print(work(N, crane_lst, M, box_lst))
