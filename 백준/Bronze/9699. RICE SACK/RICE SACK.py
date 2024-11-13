def main():
    import sys

    # 입력값
    input_lines = sys.stdin.read().splitlines()
    
    T = int(input_lines[0])
    for case_num in range(1, T + 1):
        weights = list(map(int, input_lines[case_num].strip().split()))
        max_weight = max(weights)
        
        # 출력
        print(f"Case #{case_num}: {max_weight}")

if __name__ == "__main__":
    main()
