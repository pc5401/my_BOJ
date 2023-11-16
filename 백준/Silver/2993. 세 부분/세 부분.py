if __name__ == "__main__":
    word = input().rstrip()
    n = len(word)
    lst = []

    for i in range(1, n-1):
        for j in range(i+1, n):
            a, b, c = word[:i], word[i:j], word[j:]
            lst.append(a[::-1]+b[::-1]+c[::-1])
    
    lst.sort()
    print(lst[0])