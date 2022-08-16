# 결국 구글링함ㅠㅠ
N, K = map(int ,input().split())
n = N
cnt = 0
while bin(n).count('1') > K: # 2진수로 바꿔서 1 의수를 센다. 1은 2의 배수.
    idx = bin(n)[::-1].index('1') # 1이 취치 파악해서 인덱스 
    cnt += 2 ** idx 
    n += 2 ** idx 
print(cnt)