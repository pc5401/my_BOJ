def solve(N, A, Pa, B, Pb):
    max_value = 0
    max_x = 0
    max_y = 0
    
    # Loop over possible number of tankers
    for x in range(N // Pa + 1):
        # Calculate the remaining money after hiring x tankers
        remaining_money = N - x * Pa
        
        # Calculate the maximum number of dealers we can hire with the remaining money
        y = remaining_money // Pb
        
        # Calculate the total combat power with x tankers and y dealers
        combat_power = A * x + B * y
        
        # Update max_value and corresponding x, y if a higher combat power is found
        if combat_power > max_value:
            max_value = combat_power
            max_x = x
            max_y = y
            
    return max_x, max_y

def main():
    import sys
    input = sys.stdin.readline
    N = int(input().strip())
    A, Pa, B, Pb = map(int, input().strip().split())
    result = solve(N, A, Pa, B, Pb)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
