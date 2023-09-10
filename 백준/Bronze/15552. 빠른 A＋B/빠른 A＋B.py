import sys
K = int(input())
i = 0
while i<K :
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)
    i+=1