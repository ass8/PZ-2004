import math
print("Radius : ")
rad = input()
print("Number of sides: ")
n = input()
#side length
a = math.tan(math.pi/n)*rad*2
print("Side length is :")
print(a);
print("Area is :")
print((rad*n*a)/2)
print("Perimeter is :")
print(a*n)