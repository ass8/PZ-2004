print("Input X,Y and Z: ")
x = int(input())
y = int(input())
z = int(input())
sum = x + y + z
mul = x * z * y
print("Max: ")
if(mul > sum):
    print(mul)
else:
    print(sum)
print("Min (x + y + 2/2, xyz): ")
secSum = x+y+z/2
min = secSum
if(min < mul):
    min = mul

min+=1
min = min**2
print(min)