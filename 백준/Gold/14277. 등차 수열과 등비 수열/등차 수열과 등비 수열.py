import sys
input = sys.stdin.readline

def solve(a: int, b: int, c: int, d: int, u: int) -> int:
    # 등차 수열
    count_A = 0
    if a <= u:
        count_A = (u - a) // b + 1

    # 등비 수열
    geo_terms = []
    count_G = 0
    if c <= u:
        if d == 1:
            geo_terms.append(c)
            count_G = 1
        else:
            term = c
            while term <= u:
                geo_terms.append(term)
                count_G += 1
                term *= d

    # 겹치는 항의 개수: T가 A에 속하려면 T >= a이고 (T - a) % b == 0임.
    overlap = 0
    for T in geo_terms:
        if T >= a and (T - a) % b == 0:
            overlap += 1

    return count_A + count_G - overlap

def main():
    # 입력
    a, b, c, d, u = map(int, input().split())
    
    # 풀이
    result = solve(a, b, c, d, u)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
