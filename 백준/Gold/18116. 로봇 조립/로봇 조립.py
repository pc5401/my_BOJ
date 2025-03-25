import sys
input = sys.stdin.readline

def solve(N: int, instructions: list[str]) -> list[str]:
    max_part = 10**6
    parent = list(range(max_part+1))
    comp_size = [1] * (max_part+1)
    
    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x: int, y: int) -> None:
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if comp_size[rx] < comp_size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        comp_size[rx] += comp_size[ry]
    
    result = []
    for line in instructions:
        parts = line.split()
        if parts[0] == "I":
            a = int(parts[1])
            b = int(parts[2])
            union(a, b)
        elif parts[0] == "Q":
            c = int(parts[1])
            result.append(str(comp_size[find(c)]))
    return result

def main():
    # 입력
    N = int(input().strip())
    instructions = [input().strip() for _ in range(N)]
    
    # 풀이
    result = solve(N, instructions)
    
    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
