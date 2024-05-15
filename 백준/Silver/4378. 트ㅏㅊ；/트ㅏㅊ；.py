import sys

def solve(line: str) -> str:
    keyboard = {
        '1': '`', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9', '-': '0', '=': '-',
        'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O', '[': 'P', ']': '[', '\\': ']',
        'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J', 'L': 'K', ';': 'L', "'": ';',
        'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N', ',': 'M', '.': ',', '/': '.',
        ' ': ' '  # Space remains the same
    }

    corrected_line = ''.join(keyboard.get(char, char) for char in line)
    return corrected_line

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    for line in data:
        print(solve(line))

if __name__ == "__main__":
    main()
