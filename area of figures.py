from math import sqrt
form = str (input())
if form == "треугольник":
     a = int(input())
     b = int(input())
     c = int(input())
     p = (a + b + c) / 2
     print(sqrt(p*(p-a)*(p-b)*(p-c)))
elif form == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a*b)
elif form == "круг":
    r = float (input())
    pi =3.14
    print(pi*r**2)
