from collections import defaultdict

def solution(participant, completion):
    dct = defaultdict(int)
    for p in participant:
        dct[p] += 1
        
    for c in completion:
        dct[c] -= 1
        if dct[c] == 0:
            dct.pop(c)
    ans = list(dct)[-1]
    return ans