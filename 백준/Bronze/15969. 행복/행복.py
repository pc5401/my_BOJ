def main():
    N = input()
    lst = list(map(int, input().split()))
    print(max(lst) - min(lst))
main()
