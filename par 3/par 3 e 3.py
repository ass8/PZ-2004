print("Input A,B,R and S: ")
a = float(input())
b = float(input())
r = float(input())
s = float(input())
res = a % b
if(a<=0 or b<=0 or r<=0 or s<=0):
    print("Incorrect input, please check your numbers (they may be more then 0)")
else:
    if(res == r or res == s):
        print("When dividing a non-negative integer A by a positive integer b, the remainder is equal to one of the two given numbers!")
    else:
        print("The remainder is not equal to either of the two given numbers...")