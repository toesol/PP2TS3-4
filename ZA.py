import re
select = re.compile(r"^[a-zA-Z]+@[a-zA-Z]+\.(com)|(kz)$")

while True:
     mail = input()
     if select.findall(mail):
          print("Yes")
     else:
               print("No")
