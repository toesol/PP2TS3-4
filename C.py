from math import *

def bad_number(l,r):
    str1=""
    for one in range(l,r+1):
        res=one%7
        if(res==1 or res==2 or res==5 ):
            str1=str1+str(one)+" "
    print(str1)

if __name__ == '__main__':
    l = input()
    r = input()

    bad_number(int(l),int(r))
