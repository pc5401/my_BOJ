import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        s = input().strip()
        n = len(s)
        counter = [0, 0, 0]
        l = 0
        res = float('inf')

        if n < 6:
            print(0)
            continue
        
        for r in range(n):
            if s[r].isdigit():
                counter[0] += 1
            elif s[r].islower():
                counter[1] += 1
            elif s[r].isupper():
                counter[2] += 1

            while all(val >= 1 for val in counter):
                res = min(res, r-l+1)

                if s[l].isdigit():
                    counter[0] -= 1
                elif s[l].islower():
                    counter[1] -= 1
                elif s[l].isupper():
                    counter[2] -= 1

                # Check if all categories are still present after moving the left end
                if any(val == 0 for val in counter):
                    l += 1
                    break

                l += 1
        if res < 6:
            print(6)
        elif res > n:
            print(0)
        else:
            print(res)