a = int(input())
b = int(input())
c = a * (b%10)
d = a * (b%100-b%10)
e = a * (b-b%100)
f = c+d+e
print(c)
print(d//10)
print(e//100)
print(f)