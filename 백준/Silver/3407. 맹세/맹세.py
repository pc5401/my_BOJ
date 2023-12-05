import sys
input = sys.stdin.readline

def solve(word: str):
    n = len(word)
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if word[i - 1:i] in c1 and dp[i - 1]:
            dp[i] = 1
            
        if i > 1 and word[i - 2:i] in c2 and dp[i - 2]:
            dp[i] = 1

    
    return dp[n]


if __name__ == "__main__":
    c1 = { 'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u' }
    c2 = {
	"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"
	}
    T = int(input())
    res = [0] * T
    for tc in range(T):
        res[tc] = solve(input().rstrip())
    
    for r in res:
        print('YES' if r else 'NO')