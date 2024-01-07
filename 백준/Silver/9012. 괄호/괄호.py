import sys
input = sys.stdin.readline


def VPS(words:str) -> str:
    stack = []
    for word in words:
        if word == ')' and stack:
            val = stack.pop()
            if val == '(':
                continue
            else:
                return 'NO'
        elif word == ')':
            return 'NO'
        else:
            stack.append(word)
    
    if stack:
        return 'NO'
    return 'YES'
        

if __name__ == "__main__":
    N = int(input())
    result = []
    for _ in range(N):
        words = list(input().rstrip())
        result.append(VPS(words))
    
    for res in result:
        print(res)