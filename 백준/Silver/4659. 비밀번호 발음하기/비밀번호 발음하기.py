import sys
input = sys.stdin.readline


def solve(words: list)-> int:
    pw = list(words)
    ans = True
    aeiou = dict()
    cnt = 0
    
    mo, ja = 0, 0
    for i, word in enumerate(pw):
        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if i and pw[i-1] == word and not (word == 'e' or word == 'o'):
            ans = False
            break
        
        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if word in ('a','e','i','o','u'): 
            if ja: mo, ja = 1, 0
            else: mo += 1
            cnt += 1
        else:
            if mo: mo, ja = 0, 1
            else: ja += 1
        
        if mo > 2 or ja > 2:
            ans = False
            break

    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if not cnt: 
        ans = False

    rtn = "".join(pw)
    return f'<{rtn}> is acceptable.' if ans else f'<{rtn}> is not acceptable.'

if __name__ == '__main__':
    
    res = []
    while True:
        pw = input().rstrip()
        if pw == 'end':
            break
        res.append(solve(pw))
    
    for r in res:
        print(r)