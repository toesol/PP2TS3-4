def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y,x%y)

def lcm(x,y):
  return x*y/gcd(x,y)

x,y = map(int, input().split())
n = int(gcd(x,y)+lcm(x,y))
print(n)



     