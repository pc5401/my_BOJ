T = int(input())
cute = 0
not_cute = 0
for tc in range(T):
    v = int(input())
    if v:
        cute += 1
    else:
        not_cute += 1
print("Junhee is cute!" if cute > not_cute else "Junhee is not cute!")