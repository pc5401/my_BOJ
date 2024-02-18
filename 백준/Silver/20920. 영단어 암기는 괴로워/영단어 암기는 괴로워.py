import sys
import collections
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    input_lst = [input().rstrip() for _ in range(N)]
    lst = [v for v in input_lst if len(v)>=M]
    cnt_dict = collections.Counter(lst)

    word_cnt = [ (k,i) for k,i in cnt_dict.items()]
    word_cnt.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word, cnt in word_cnt:
        print(word)
