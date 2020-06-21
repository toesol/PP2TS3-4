s = input()
b = []
for i in s:
    if i.isalpha() and (i.upper() not in b) and (i.lower() not in b):
        b.append(i)
str = "".join(b)
print(str)


