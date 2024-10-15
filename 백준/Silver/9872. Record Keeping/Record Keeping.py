import sys
input = sys.stdin.readline   

if __name__ == "__main__":
    N = int(input())
    count_cow = dict()
    for i in range(N):
        group = '-'.join(sorted(input().rstrip().split()))
        if count_cow.get(group):
            count_cow[group] += 1
        else:
            count_cow[group] = 1
    
    result = 0
    for cnt in count_cow.values():
        if cnt > result:
            result = cnt
    print(result)