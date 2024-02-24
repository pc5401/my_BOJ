import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    keywords = {input().rstrip() for _ in range(N)}
    used = [input().rstrip().split(',') for _ in range(M)]
    
    n = N
    for used_keywords in used:
        for keyword in used_keywords:
            if keyword in keywords:
                n -= 1
                keywords.remove(keyword)
        print(n)