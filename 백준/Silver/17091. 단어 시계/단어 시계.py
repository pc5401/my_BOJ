import sys
input = sys.stdin.readline

num_words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two",
    23: "twenty three", 24: "twenty four", 25: "twenty five",
    26: "twenty six", 27: "twenty seven", 28: "twenty eight",
    29: "twenty nine", 30: "thirty"
}

def solve(h: int, m: int) -> str:
    if m == 0:
        return f"{num_words[h]} o' clock"
    if m == 15:
        return f"quarter past {num_words[h]}"
    if m == 30:
        return f"half past {num_words[h]}"
    if m == 45:
        nh = h + 1 if h < 12 else 1
        return f"quarter to {num_words[nh]}"
    if m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{num_words[m]} {minute_word} past {num_words[h]}"

    mm = 60 - m
    minute_word = "minute" if mm == 1 else "minutes"
    nh = h + 1 if h < 12 else 1
    return f"{num_words[mm]} {minute_word} to {num_words[nh]}"

def main():
    # 입력
    h = int(input().strip())
    m = int(input().strip())
    # 풀이
    result = solve(h, m)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
