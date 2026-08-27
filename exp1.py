# user input information
a = int(input("enter the first num:"))
b = int(input("enter the last num:"))
# adding the first and last num
print(a+b, "addition of num1 & num2")
print(a-b, "subtraction of num1 & num2")
print(a**b, "num2 power num1")

if b != 0:
    print(a/b, "division of num1 by num2")
else:
    print("invalid input")
