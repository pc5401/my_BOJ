import sys
input = sys.stdin.readline

def final_DNA(N: int, DNA: str) -> int:
    AGCT_table = {
        'A': {'A':'A', 'G':'C','C':'A','T':'G'},
        'G': {'A':'C', 'G':'G','C':'T','T':'A'},
        'C': {'A':'A', 'G':'T','C':'C','T':'G'},
        'T': {'A':'G', 'G':'A','C':'G','T':'T'}
    }
    Q = [dna for dna in DNA]

    last_dna = Q.pop()
    while Q:
        second_last = Q.pop()
        last_dna = AGCT_table[last_dna][second_last]

    return last_dna


def main():
    # 입력값
    N: int = int(input())
    DNA: str = input().rstrip()
    print(final_DNA(N, DNA))


if __name__ == "__main__":
    main()
