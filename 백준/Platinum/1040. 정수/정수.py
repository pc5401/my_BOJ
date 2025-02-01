# chatGPT o3-mini test

def solve():
    import sys
    sys.setrecursionlimit(10000)
    from functools import lru_cache

    input = sys.stdin.readline
    data = input().strip().split()
    if not data:
        return
    N_str, K_str = data
    N = int(N_str)
    K = int(K_str)
    s = str(N)
    
    # 정답의 자릿수 L은 최소 max(len(s), K) 자리부터 시작합니다.
    startL = max(len(s), K)
    # N이 최대 10^18이므로 최대 19자리까지 나오지만, 경우에 따라 한 자릿수 더 필요한 경우도 있으므로 충분히 큰 상한을 둡니다.
    for L in range(startL, 23):
        # L이 N과 자릿수가 같으면 lowerBound로 s를 사용하고,
        # L이 더 크면 하한 조건이 없으므로 lowerBound는 None입니다.
        lowerBound = s if L == len(s) else None

        @lru_cache(maxsize=None)
        def rec(pos, tight, mask):
            """
            pos   : 현재 자릿수 (0부터 L-1까지)
            tight : 현재까지 lowerBound와 일치하는지 여부 (1이면 일치, 0이면 이미 더 큰 상태)
            mask  : 지금까지 사용한 숫자들을 비트마스크로 표현 (예, d번째 비트가 1이면 d 사용)
            
            L자리 수의 나머지 부분을 결정하여 조건을 만족하는 최소 수의 문자열(접미사)를 반환.
            불가능하면 None을 반환.
            """
            if pos == L:
                # 모든 자릿수를 결정한 후, 사용한 숫자의 개수가 정확히 K여야 함.
                if mask.bit_count() == K:
                    return ""
                else:
                    return None
            
            # lowerBound가 주어지고 아직 tight 상태이면, 현재 자릿수에 사용할 최소 숫자는 lowerBound[pos]
            # 그렇지 않으면, 첫 자리는 0이 허용되지 않으므로 (pos==0이면) 최소 1, 그 외는 0부터 가능합니다.
            if lowerBound is not None and tight:
                lo = int(lowerBound[pos])
            else:
                lo = 1 if pos == 0 else 0

            # 가능한 숫자 d를 lo부터 9까지 시도합니다.
            for d in range(lo, 10):
                new_mask = mask | (1 << d)
                cnt = new_mask.bit_count()
                # 지금까지 사용한 숫자가 K개를 초과하면 패스
                if cnt > K:
                    continue
                # 남은 자릿수 모두가 서로 다른 숫자로 채워진다고 하더라도 
                # (최대 남은 자리수 개수 = L-pos-1) 총 개수가 K에 미치지 못하면 불가능
                remaining = L - pos - 1
                if cnt + remaining < K:
                    continue
                # tight 상태 갱신: 만약 지금까지 lowerBound와 일치했고 선택한 d가 lowerBound[pos]와 같으면 계속 tight
                new_tight = 1 if (lowerBound is not None and tight and d == int(lowerBound[pos])) else 0
                sub = rec(pos + 1, new_tight, new_mask)
                if sub is not None:
                    return str(d) + sub
            return None

        ans = rec(0, 1 if lowerBound is not None else 0, 0)
        if ans is not None:
            sys.stdout.write(ans)
            return

if __name__ == '__main__':
    solve()
