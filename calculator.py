a = float (input())
b = float (input())
d = str (input())
if d == "+" :
  print(a+b)
elif d == "-":
  print(a-b) 
elif d == "*": 
  print(a*b)
elif d == "mod" and b != 0:
  print(a%b)
elif d == "mod" and b == 0:
  print("Деление на 0!")
elif d == "pow":
   print(a**b)
elif d == "diw" and b == 0:
  print("Деление на 0!")
elif d == "diw" and b != 0:
  print(a//b)
elif d == "/" and b == 0:
   print("Деление на 0!")
elif d == '/' and b != 0: 
  print(a/b)
