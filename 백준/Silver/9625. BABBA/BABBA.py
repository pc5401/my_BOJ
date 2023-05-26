N = int(input())
click = lambda x,y : (y, x+y)
A,B = 1,0 # A, B
for i in range(N):
    A,B = click(A,B)
print(A,B)