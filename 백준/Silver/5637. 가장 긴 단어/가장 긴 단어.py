import re

def solve(text:list):
    text = ' '.join(text)
    words = re.findall('[a-zA-Z-]+', text)  # Extract words
    ans = max(words, key=len)  # Find the longest word
    return ans.lower()


if __name__ == '__main__':
    lst = []
    while True:
        line = input()
        if 'E-N-D' in line:
            lst.append(line[:line.index('E-N-D')])
            break
        else:
            lst.append(line)
    res = solve(lst)
    print(res)