import sys
input = sys.stdin.read

m = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
     'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
     'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','_':'..--',',':'.-.-','.':'---.','?':'----'}
r = {v:k for k,v in m.items()}

def solve(lines):
    result = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        s, L = '', ''
        for c in line:
            code = m[c]
            s += code
            L += str(len(code))
        L = L[::-1]
        i = 0
        ans = ''
        for d in L:
            l = int(d)
            ans += r[s[i:i+l]]
            i += l
        result.append(ans)
    return result

def main():
    lines = input().split('\n')
    
    result = solve(lines)

    for res in result:
        print(res)

if __name__ == "__main__":
    main()