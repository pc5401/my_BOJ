import sys
input = sys.stdin.readline

def create_square(N, M, arr):
    num = max(N, M)
    p = 1
    while p < num:
        p <<= 1
    num = p
    return [[arr[i][j] if i < N and j < M else 0 for j in range(num)] for i in range(num)], num

def build_quadtree(r1, c1, r2, c2):
    all_one = True
    all_zero = True
    for i in range(r1, r2):
        for j in range(c1, c2):
            if sqr[i][j] == 1:
                all_zero = False
            else:
                all_one = False
            if not all_one and not all_zero:
                break
        if not all_one and not all_zero:
            break

    if all_one:
        result['1'] = result.get('1', 0) + 1
        return '1'
    if all_zero:
        result['0'] = result.get('0', 0) + 1
        return '0'

    mid_r = (r1 + r2) // 2
    mid_c = (c1 + c2) // 2
    c1_res = build_quadtree(r1, c1, mid_r, mid_c)
    c2_res = build_quadtree(r1, mid_c, mid_r, c2)
    c3_res = build_quadtree(mid_r, c1, r2, mid_c)
    c4_res = build_quadtree(mid_r, mid_c, r2, c2)
    val = 'X' + c1_res + c2_res + c3_res + c4_res
    result[val] = result.get(val, 0) + 1
    return val

def parse_tree(word, idx=0):
    if word[idx] in ('0', '1'):
        return word[idx], idx+1
    else:
        idx += 1
        c1, idx = parse_tree(word, idx)
        c2, idx = parse_tree(word, idx)
        c3, idx = parse_tree(word, idx)
        c4, idx = parse_tree(word, idx)
        return 'X' + c1 + c2 + c3 + c4, idx

def parse_subtrees(word):
    assert word[0] == 'X'
    idx = 1
    c1, idx = parse_tree(word, idx)
    c2, idx = parse_tree(word, idx)
    c3, idx = parse_tree(word, idx)
    c4, idx = parse_tree(word, idx)
    return 'X' + c1 + c2 + c3 + c4, [c1, c2, c3, c4]

def restore_count(word, remove_count):
    if word in ('0', '1'):
        if result.get(word, 0) >= remove_count:
            result[word] -= remove_count
        else:
            result[word] = 0
        return
    if word not in result:
        return
    if result[word] >= remove_count:
        result[word] -= remove_count
    else:
        result[word] = 0
    if word.startswith('X'):
        _, children = parse_subtrees(word)
        for c in children:
            restore_count(c, remove_count)

def cutting(word):
    count = result.get(word, 0)
    if count <= 1:
        return
    remove_count = count - 1
    result[word] = 1
    _, children = parse_subtrees(word)
    for c in children:
        restore_count(c, remove_count)

def get_result():
    key_lst = list(result.keys())
    key_lst.sort(key=len, reverse=True)
    for key in key_lst:
        if key in ('0', '1'):
            continue
        while result.get(key, 0) > 1:
            cutting(key)

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, list(input().strip()))) for _ in range(N)]
    sqr, L = create_square(N, M, arr)
    result = dict()

    top = build_quadtree(0, 0, L, L)
    res1 = sum(result.values())
    get_result()
    res2 = sum(result.values())
    print(res1, res2)
