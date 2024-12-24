import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    even_first_digits = [2, 4, 6, 8]
    even_other_digits = [0, 2, 4, 6, 8]
    
    k = 1
    while True:
        total = 5**k - 1
        if total >= N:
            break
        k += 1
    
    previous_total = 5**(k-1) - 1
    pos = N - previous_total
    pos -= 1  # zero-based indexing
    
    if k == 1:
        return even_first_digits[pos]
    else:
        first_digit_index = pos // (5**(k-1))
        first_digit = even_first_digits[first_digit_index]
        remaining = pos % (5**(k-1))
        
        digits = []
        for _ in range(k-1):
            digits.append(remaining % 5)
            remaining //= 5
        digits = digits[::-1]
        
        number_str = str(first_digit) + ''.join(str(even_other_digits[d]) for d in digits)
        return int(number_str)

def main():
    N = int(input())
    result = solve(N)
    print(result)

if __name__ == "__main__":
        main()
