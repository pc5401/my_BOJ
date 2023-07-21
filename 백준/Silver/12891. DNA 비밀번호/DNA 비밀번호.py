import sys
input = sys.stdin.readline

def func(a,c,g,t):

    if data["A"] < a:
        return 0
    elif data["C"] < c:
        return 0
    elif data['G'] < g:
        return 0
    elif data["T"] < t:
        return 0
    
    return 1

if __name__ == "__main__":
    S, P = map(int,input().split())
    words = input().strip()
    A, C, G, T = map(int,input().split())
    res = 0 # 갯수 확인
    data = {"A":0, "C":0, "G":0, "T":0}
    for i in words[0:P]:
        if i in 'ACGT':
            data[i] += 1
    res += func(A, C, G, T)
    for i in range(P,S):
        j = i - P
        if words[j] in 'ACGT':
            data[words[j]] -= 1

        if words[i] in 'ACGT':
            data[words[i]] += 1
            
        res += func(A, C, G, T)

    print(res)