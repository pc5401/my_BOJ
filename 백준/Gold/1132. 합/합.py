import sys
import collections
input = sys.stdin.readline


def make_points(words: list[str]) -> dict:
    """ 알파벳의 자리를 수의 자리로 치환해 점수화 
    Args: 
        words (list[str]) : 리스트화된 문자

    Returns:
        dict : 알파벳별 점수
    """
    rtn = collections.defaultdict(int)

    for word in words:
        for i in range(1, len(word)+1):
            rtn[word[-i]] += 10**(i-1)

    return rtn


def make_nums(points: dict[int], not_zero: list[str]) -> dict:
    ranks = [[key, val] for key, val in points.items()]
    ranks.sort(key=lambda x : -x[1])
    
    for i in range(len(ranks)):
        ranks[i][1] = 9 - i
    
    idx = 1
    while len(ranks) > 9:
        if ranks[-1][0] in not_zero:
            ranks[-1][0], ranks[-1-idx][0] = ranks[-1-idx][0], ranks[-1][0]
            idx += 1
        else:
            break

    return {alpa : val for alpa, val in ranks}
    


def cnt_num(nums: dict, word: list[str]) -> int:
    lst = [str(nums[w]) for w in word]
    return int("".join(lst))


if __name__ == "__main__":
    N = int(input())
    words = [list(input().rstrip()) for _ in range(N)]
    points = make_points(words)
    not_zero = [words[i][0] for i in range(N)]
    nums = make_nums(points, not_zero)
    
    res = 0
    for word in words:
        res += cnt_num(nums, word)
    print(res)