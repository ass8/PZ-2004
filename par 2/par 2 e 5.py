print("Input A,B and C: ")
a = int(input())
b = int(input())
c = int(input())

if(a>=b and b>=c):
    a *= 2
    b *= 2
    c *= 2
    print(a,b,c)
    print("Неравенства выполняются")
else:
   a = abs(a)
   b = abs(b)
   c = abs(c)
   print(a, b, c)
   print("Неравенства не выполняются")