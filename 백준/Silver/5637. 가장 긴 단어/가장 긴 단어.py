import sys
import re

input = sys.stdin.readline

def main():
    max_len = 0
    result = ''
    lines = ''

    for line in sys.stdin:
        lines += line
    
    for word in re.findall('[a-zA-Z-]+', lines):
        if len(word) > max_len:
            max_len = len(word)
            result = word
    
    print(result.lower())


if __name__ == "__main__":
    main()