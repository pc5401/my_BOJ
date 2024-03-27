import sys

input = sys.stdin.readline

def func(target: str, lst: list[str])-> str:
    M = len(target)
    rtn = ''
    rtn_len = 0
    
    for word in lst:
        m = min(M, len(word))
        cnt = 0
        for j in range(m):
            if target[j] == word[j]:
                cnt += 1
            else:
                break
        
        if cnt > rtn_len:
            rtn = word
            rtn_len = cnt

    return rtn, rtn_len


def main():
    N = int(input())
    word_lst = [input().rstrip() for _ in range(N)]
    
    longest_len = 0
    result = ['', '']

    for i in range(N-1):
        word, word_len = func(word_lst[i], word_lst[i+1:])

        if word_len > longest_len:
            longest_len = word_len
            result[0] = word_lst[i]
            result[1] = word

    for res in result:
        print(res)

if __name__ == "__main__":
    main()
