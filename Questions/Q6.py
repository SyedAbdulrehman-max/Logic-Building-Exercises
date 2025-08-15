#Calculate the factorial of a number without using the math module.
# n = int(input("enter the number: "))

# if n<0:
#     print("The factorial number is not define: ")
# else:
#     factorial = 1
#     i = 1
#     while i <= n :
#         factorial *=1
#         i +=1
#         print(f"{n} != {factorial}")
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"{n}! = {factorial}")