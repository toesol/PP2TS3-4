def temur(a,b):
    if a == 1 or b == 1:
        return 1
    return temur(a-1,b) + temur(a,b-1)

a,b =map(int, input().split())
print(temur(a,b))