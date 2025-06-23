import sys
input = sys.stdin.readline

def solve(names: list[str]) -> list[str]:
    odd = names[::2]
    even = names[1::2][::-1]
    return odd + even

def main():
    # 입력
    outputs = []
    set_no = 1
    while True:
        n = int(input().strip())
        if n == 0:
            break
        names = [input().rstrip('\n') for _ in range(n)]
        # 풀이
        ordered = solve(names)
        outputs.append(f"SET {set_no}")
        outputs.extend(ordered)
        set_no += 1
    # 출력
    print("\n".join(outputs))

if __name__ == "__main__":
    main()
