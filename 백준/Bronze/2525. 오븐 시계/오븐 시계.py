x,y = map(int, input().split())
z = int(input())
if y+z<60 :
    print(x,y+z,sep=' ')
else :
    if x+(y+z)//60 >= 24 :
        print(x+(y+z)//60-24,y+z-(60*((y+z)//60)),sep=' ')
    else :
        print(x+(y+z)//60,y+z-(60*((y+z)//60)),sep=' ') 