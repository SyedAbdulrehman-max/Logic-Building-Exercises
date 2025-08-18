# 23. Find the largest number in a list of 5 numbers.
numbers =[2,3,4,2,3]
larger = numbers[0]
for i in numbers:
    if i > larger:
     larger = i
    

print(larger)