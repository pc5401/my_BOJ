import sys
input = sys.stdin.readline

def solve(v: str) -> str:
    mapping = {
        'A': 'a',
        'B': 'v',
        'E': 'ye',
        'K': 'k',
        'M': 'm',
        'H': 'n',
        'O': 'o',
        'P': 'r',
        'C': 's',
        'T': 't',
        'Y': 'u',
        'X': 'h'
    }
    rtn = []
    for char in v:
        rtn.append(mapping[char]) 
    return ''.join(rtn)

if __name__ == "__main__":
    v = input().rstrip()
    result = solve(v)
    print(result)
