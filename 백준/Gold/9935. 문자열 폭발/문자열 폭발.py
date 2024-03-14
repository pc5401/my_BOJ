def main():
    chars = input().rstrip()
    bomb = input().rstrip()

    n, m = len(chars), len(bomb)
    
    stack = []

    for i in range(n):
        l = len(stack)
        if l >= m and stack[-1] == bomb[-1]:
            if "".join(stack[l-m:]) == bomb:
                for _ in range(m):
                    stack.pop()
        stack.append(chars[i])

    l = len(stack)
    if l >= m and stack[-1] == bomb[-1]:
        if "".join(stack[l-m:]) == bomb:
            for _ in range(m):
                stack.pop()

    result = "".join(stack)
    if not result:
        print('FRULA')
    else:
        print(result)

if __name__ == "__main__":
    main()
