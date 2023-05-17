def solution(s):
    answer = True
    stack = []
    for w in s:
        if w == "(":
            stack.append(w)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return False if stack else True 