import sys

input = sys.stdin.readline

def solve(votes: str) -> str:
    total = len(votes)

    absent = votes.count('A')

    if absent * 2 >= total:

        return "need quorum"

    yes = votes.count('Y')

    no  = votes.count('N')

    if yes > no:

        return "yes"

    if no > yes:

        return "no"

    return "tie"

def main():

    results = []

    while True:

        line = input().strip()

        if line == "#" or not line:

            break

        # 풀이

        res = solve(line)

        results.append(res)

    # 출력

    print("\n".join(results))

if __name__ == "__main__":

    main()