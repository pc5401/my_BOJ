import sys

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0

    # 첫 줄: n1, n2, n3
    n1, n2, n3 = map(int, input[idx:idx+3])
    idx += 3

    # 순서 유지 리스트
    order = []
    seen = set()

    # 각 매장의 판매량을 저장할 딕셔너리
    store1 = {}
    store2 = {}
    store3 = {}

    # 첫 번째 매장
    for _ in range(n1):
        id_num = input[idx]
        units = int(input[idx+1])
        idx += 2
        if id_num not in store1:
            store1[id_num] = 0
        store1[id_num] += units

        # 순서 기록
        if id_num not in seen:
            seen.add(id_num)
            order.append(id_num)

    # 두 번째 매장
    for _ in range(n2):
        id_num = input[idx]
        units = int(input[idx+1])
        idx += 2
        if id_num not in store2:
            store2[id_num] = 0
        store2[id_num] += units

        # 순서 기록
        if id_num not in seen:
            seen.add(id_num)
            order.append(id_num)

    # 세 번째 매장
    for _ in range(n3):
        id_num = input[idx]
        units = int(input[idx+1])
        idx += 2
        if id_num not in store3:
            store3[id_num] = 0
        store3[id_num] += units

        # 순서 기록
        if id_num not in seen:
            seen.add(id_num)
            order.append(id_num)

    # 모든 매장에서 20개 이상 판매된 아이템 찾기
    result_ids = []
    for id_num in order:
        cnt1 = store1.get(id_num, 0)
        cnt2 = store2.get(id_num, 0)
        cnt3 = store3.get(id_num, 0)
        if cnt1 >= 20 and cnt2 >= 20 and cnt3 >= 20:
            result_ids.append(id_num)

    # 출력
    print(len(result_ids), end='')
    if result_ids:
        print(' ' + ' '.join(result_ids))
    else:
        print()

if __name__ == "__main__":
    main()
