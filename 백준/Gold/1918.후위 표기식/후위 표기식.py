strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)

# 테스트용
# 출처: https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python [박지원]