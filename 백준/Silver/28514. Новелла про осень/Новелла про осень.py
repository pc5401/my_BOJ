import sys
input = sys.stdin.readline


def keyboard(keys: str) -> dict[str, set]:
    rtn = {keys[-1] : {keys[0]}}
    n = len(keys)

    for i, key in enumerate(keys, start=1):
        if key in rtn and i < n:
            rtn[key].add(keys[i])
        elif i < n:
            rtn[key] = {keys[i]}
    return rtn


def solve(keys: dict[str, set], novel: str) -> bool:

    if not novel[0] in keys:
        return False

    for i in range(len(novel)-1):
        word = novel[i]
        if not novel[i+1] in keys[word]:
            return False
    
    return True


def main():
    # 입력값
    N = int(input())
    keys = input().rstrip()
    novel = input().rstrip()
    
    # 풀이
    result = solve(keyboard(keys), novel)
    
    # 출력
    print('YES' if result else 'NO')

if __name__ == '__main__':
    main()
