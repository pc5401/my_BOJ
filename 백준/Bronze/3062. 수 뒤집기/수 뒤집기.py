T = int(input())
input_lst = [ input() for _ in range(T)]

sum_values = [ str(int(v) + int(v[::-1])) for v in input_lst]

result = [ 'YES' if v == v[::-1] else 'NO' for v in sum_values]

for res in result:
    print(res)

