T = int(input())
for tc in range(T):
    lst = list(input().split())
    a = lst[0:2]
    b = lst[2:]
    
    print(" ".join(b) + " " + " ".join(a))