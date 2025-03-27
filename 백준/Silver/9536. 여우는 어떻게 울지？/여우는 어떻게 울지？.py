import sys
input = sys.stdin.readline

def solve(noise, animal_lines):
    known_sounds = set()
    
    for line in animal_lines:
        parts = line.split()
        sound = parts[-1]
        known_sounds.add(sound)
    
    fox_sounds = [s for s in noise if s not in known_sounds]
    
    return ' '.join(fox_sounds)

def main():
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        noise = input().strip().split()
        animal_lines = []
        
        while True:
            line = input().rstrip()
            if line == 'what does the fox say?':
                break
            animal_lines.append(line)
        
        result = solve(noise, animal_lines)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
