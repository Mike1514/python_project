#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
f = int (input())
s = int (input())
t = int (input())
a = max(f, s, t)
b = min(f, s, t)
print(a)
print(b)
if a == f and b == s or a == s and b == f:
    print(t)
elif a == t and b == f or a == f and b == t:
    print(s)
elif a == s and b == t or a == t and b == s:
    print(f)
