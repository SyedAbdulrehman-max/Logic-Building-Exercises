# Ask the user for a number n and print the sum of all numbers from 1 to n.

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print(f"The sum of numbers {n} is {sum}")