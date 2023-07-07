import sys
input = sys.stdin.readline


class BIT: # Binary Indexed Tree = Fenwick Tree
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size+1)]

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += (i & -i)
    
    def get_sum(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= (i & -i)
        return result


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    arr2 = sorted(arr)
    
    # 값의 원래 순서를 dict으로 저장
    dic = {v: i+1 for i, v in enumerate(arr2)}
    
    ft = BIT(N)
    answer = 0
    for a in arr[::-1]:
        num = dic[a]
        ft.update(num, 1)
        answer += ft.get_sum(num-1)
    
    print(answer)