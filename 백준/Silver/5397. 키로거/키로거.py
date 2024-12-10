import sys
input = sys.stdin.readline

def solve(l: int, keys: str) -> str:
    left, right = [], []

    for key in keys:
        if key == '-' and left:
            left.pop()
        
        elif key == '<' and left:
            word = left.pop()
            right.append(word)
        
        elif key == '>' and right:
            word = right.pop()
            left.append(word)

        elif key == '-' or key == '>' or key == '<':
            continue

        else:
            left.append(key)

    while right:
        r = right.pop()
        left.append(r)

    return "".join(left)
    

if __name__ == "__main__":
    T = int(input())
    L = [input().rstrip() for _ in range(T)]
    
    # 풀이
    result = [solve(len(L[t]), L[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(res)
