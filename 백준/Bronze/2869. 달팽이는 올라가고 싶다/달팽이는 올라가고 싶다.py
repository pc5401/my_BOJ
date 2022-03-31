import math

A, B, V = map(int, input().split())

up = A - B
top = V - B

print(math.ceil(top/up))