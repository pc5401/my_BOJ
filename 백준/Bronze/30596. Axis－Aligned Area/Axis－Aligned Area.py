import sys
input = sys.stdin.readline

def main():
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    a4 = int(input())
    
    max_area = min(a1, a2) * min(a3, a4)
    
    print(max_area)

if __name__ == "__main__":
    main()

