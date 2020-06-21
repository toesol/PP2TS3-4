def convertToBase7(num):
    x = abs(num)
    result = ""
    while True:
        remainder = x % 7
        x //= 7
        result += str(remainder)
        if x == 0:
            break
    if num<0:
        result += "-"
    result = result[::-1]
    return result
num = int(input())
print(convertToBase7(num))