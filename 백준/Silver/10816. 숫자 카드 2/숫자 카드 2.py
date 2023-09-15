import sys
import bisect
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    my_cards = sorted(list(map(int,input().split())))
    M = int(input())
    look_for = list(map(int, input().split()))
    res_list = [0] * M

    for idx, card in enumerate(look_for):
        lo = bisect.bisect_left(my_cards, card)
        hi = bisect.bisect_right(my_cards, card)
        res_list[idx] = hi - lo

    print(*res_list)