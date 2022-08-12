lst = list(map(int, input()))
change_lst = sorted(lst, reverse=True)
res = "".join(list(map(str, change_lst)))
print(res)