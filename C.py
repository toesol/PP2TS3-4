l,r=map(int,input().split())

for x in range(l,r+1):
    a = x%7
    if a==1 or a==2 or a==5:
        
        print(x,end=' ')
