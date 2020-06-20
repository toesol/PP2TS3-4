import re

select = re.compile(r"\d")
while True:
    sum = 0
    number = input()
    if number.isdigit():
        num_lst = select.findall(number)
        if num_lst:
            for num in num_lst:
                sum += int(num)
    else:
        print()
    if sum % 4 == 0 and sum != 0:
        print("Yes")
    else:
        print("No")

