import sys
input = sys.stdin.readline

def solve() -> list[str]:
    cube = [0] * 101
    for i in range(2, 101):
        cube[i] = i * i * i
    result = []
    for a in range(2, 101):
        for b in range(2, a - 1):
            for c in range(b + 1, a):
                for d in range(c + 1, a):
                    if cube[b] + cube[c] + cube[d] == cube[a]:
                        result.append(f"Cube = {a}, Triple = ({b},{c},{d})")
    return result

def main():
    # 입력X
    result = solve()
    
    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
