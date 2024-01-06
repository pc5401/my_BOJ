import sys
input = sys.stdin.readline

def solve(snt: str) -> str: # 최대공약수
    
    stack = []
    for s in snt:
        if s.isalpha():
            continue
        
        if s == ')' and stack:
            stack_val = stack.pop()
            if stack_val == '(':
                continue
        
        elif s == ']' and stack:
            stack_val = stack.pop()
            if stack_val == '[':
                continue
        
        elif s == '.' and stack:
            return 'no'
        
        elif s == '.':
            return 'yes'
        
        else:
            stack.append(s)
            continue

        return 'no'
    
    return 'no'

if __name__ == "__main__":
    while 1:
        snt = input().rstrip()
        if snt == '.':
            break
        print(solve(snt.replace(" ", "")))
