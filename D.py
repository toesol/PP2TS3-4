def Tribonacci(n):
    temp = {0:0,1:1,2:1}
    if n in temp:
        return temp[n]
    rst = [0]*(n+1)
    rst[0], rst[1], rst[2] = 0,1,1
    for i in range(3 ,n+1):
        rst[i] = rst[i-1] +rst[i-2] +rst[i-3]
    return rst[n]

n = int(input())
print(Tribonacci(n))
