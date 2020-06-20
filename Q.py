number = input()
a = number % 10
b = number // 10 % 10
c = number // 100 % 10
d = number // 1000

def esf(e):
for e in range(number):
    e = a + b + c + d
if e%4 == 0:
    print "Yes" 
else:
    print "No" 
