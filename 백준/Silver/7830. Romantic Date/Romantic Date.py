import sys
input = sys.stdin.readline

num_rank = {c: i for i, c in enumerate("23456789TJQKA")}
suit_rank = {c: i for i, c in enumerate("DCHS")}

def encode(card):
    v, s = card[0], card[1]
    return num_rank[v] * 4 + suit_rank[s]

def solve(hand_tokens):
    w = [encode(x) for x in hand_tokens]
    used = [False] * 52
    for x in w:
        used[x] = True
    opp = [i for i in range(52) if not used[i]]
    w.sort()
    opp.sort()
    i = j = 0
    win = 0
    while j < 26 and i < 26:
        if w[j] > opp[i]:
            win += 1
            i += 1
            j += 1
        else:
            j += 1
    return win

def main():
    # 입력
    T = int(input())
    outs = []
    for _ in range(T):
        tokens = []
        while len(tokens) < 26:
            line = input().strip()
            if not line:
                continue
            tokens.extend(line.split())
        tokens = tokens[:26]

        # 풀이
        result = solve(tokens)

        # 출력
        outs.append(str(result))
    print("\n".join(outs))

if __name__ == "__main__":
    main()
