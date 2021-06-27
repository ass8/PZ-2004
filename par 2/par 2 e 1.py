''' a) '''
x = input()
y = input()
max = 0
if(x>y):
    max = x
else:
    if(x<y):
        max = y
print("MAX = ", max)
''' б) '''
x = input()
y = input()
min = 0
if(x>y):
    min = y
else:
    if(x<y):
        min = x
print("MIN = ", min)

''' в) '''
x = input()
y = input()
min = 0
if(x>y):
    min = y
    max = x
else:
    if(x<y):
        min = x
        max = y
print("MAX = ", max," MIN = ", min)