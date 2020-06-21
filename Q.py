def func(num):
    if num < 10:
        return num
    else:
        return func(num // 10) + func(num % 10)


num = int(input())
c = num%10
res = func(num)
if res%c == 0:
    print("Yes")
else:
    print("No")


