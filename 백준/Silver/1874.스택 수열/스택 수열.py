# MyStack 클래스를 만들자.

class MyStack:
    def __init__(self):
        self.items = [] # 데이터를 저장할 리스트

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try: #pop할 아이템이 없으면 IndexError 가 발생하기 때문에
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return "Stack is empty"

    def __len__(self): # len()으로 호출하면 stack의 item 수 반환
        return len(self.items)

    def isEmpyt(self):
        return len(self) == 0

# 입력 처리
n = int(input())
lst = []
for i in range(1, n+1):
    data = int(input())
    lst.append(data)

stack = MyStack()
cnt = 0
number = 0
box = [int(i) for i in range(1, n+1)]
ans = []
flag = 'suss'


while 1:
    target = lst[0]
    if stack.top() != target:
        try:
            ans.append('+')
            stack.push(box.pop(0))
        except IndexError:
            flag = 'fail'
            break

    elif stack.top() == target:
        ans.append('-')
        lst.pop(0)
        stack.pop()
        if stack.top() =='Stack is empty' and len(box) == 0:
            flag = 'suss'
            break

if flag == 'suss':
    for a in ans:
        print(a)
elif flag == 'fail':
    print('NO')