# 14. Print sum of first n numbers (user input).d
user = int(input("Enter a number: "))
total = 0
count= 1
for i in range(1,user+1):
    total+=i
    count +=1
    # print(total)
    
print(total)