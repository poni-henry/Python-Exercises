"""Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message"""

num = int(input("Please input an odd or even number: "))

#modulo division sign is %
#check for divisible by 4 first before by 2

if  num%4==0:
    print("number is a multiple of 4")
elif num%2==0:
    print("the number is even")
else:
    print("The number is odd")

'''Checking if a number is divisible by another'''

num_1 = int(input("Please input numerator: "))
num_2 = int(input("Please input denominator: "))

if num_1 % num_2 ==0:
    print(str(num_1) + " is divisible by " + str(num_2))
else:
    print(str(num_1) + " is not divisible by " + str(num_2))
