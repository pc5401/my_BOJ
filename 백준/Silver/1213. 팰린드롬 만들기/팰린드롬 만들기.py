import sys
input = sys.stdin.readline

def func():
    start, mid, end = '', '', ''

    if len(words) == 1:
        return words[0]
    
    while len(words) > 1:
        x = words.pop()
        y = words.pop()

        if x == y:
            start = x + start
            end = end + y

        else:
            if len(words) == 0:
                return "I'm Sorry Hansoo"
            z = words.pop()
            if z == y:
                mid += x
                start = y + start
                end = end + z
            else:
                return "I'm Sorry Hansoo"
            
    if words:
        mid += words[0]

    if len(mid) > 1:
        return "I'm Sorry Hansoo"

    return start + mid + end


if __name__ == '__main__':
    input_words = list(input().strip())
    words = sorted(input_words)
    print(func())

