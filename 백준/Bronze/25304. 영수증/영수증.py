X = int(input())
N = int(input())
i=1
k=0
while i<=N :
    a, b = map(int,input().split())
    k += a*b
    i+=1
if X==k :
    print("Yes")
else :
    print("No")