def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

print("Input N: ")
n = int(input())
mas = []

if(n>99):
    print("Incorrect input, please check your numbers (they may be more then 99)")
else:

    mas = get_pos_nums(n)
    sum = mas[0] + mas[1]
    sum = sum** 3
    n = n** 2
    if(n == sum):
       print("Expression is correct")
    else:
       print("Expression is not correct")