
# 35. Take numbers from user until 0; print their sum.

total = 0   # to store the sum

while True:   # infinite loop until user enters 0
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:   # stop when 0 entered
        break
    total += num   # add number to sum

print("Sum of numbers is:", total)
