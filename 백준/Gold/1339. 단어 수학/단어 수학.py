from collections import defaultdict
dic = defaultdict(list)
for s in ['A','B','C','D','E','F','G','H','I','J','K','N','M','L','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    dic[s] = [0]*8
words = []
lst = []
N = int(input())
for i in range(N):
    data = input()
    for d in data:
        if not d in words:
            words.append(d)

    lst.append(data)
    s = len(data)
    for j in range(s-1,-1,-1):
        dic[data[j]][s-j-1] += 1


nums = defaultdict(int)
for s in words:
    # nums[s] = int("".join(map(str, dic[s][::-1])))
    sumValue = 0
    for i, v in enumerate(dic[s]):
        sumValue += v * (10 ** i)
    nums[s] = sumValue
nums_sorted = sorted(nums.items(), key=lambda x:x[1])  # 오름차순 정렬


res = defaultdict(int)
x = 10 - len(nums_sorted)
for  i,word in enumerate(nums_sorted):
    res[word[0]] = i + x


# print(res)
sumV = 0
for i in lst:
    i_lst = list(i)
    for j, word in enumerate(i_lst):
        i_lst[j] = str(res[word])
    value = int("".join(i_lst))
    sumV += value

print(sumV)

