# Print the first n numbers of the Fibonacci sequence.

n = int(input("Enter the number: "))

a = 0
b = 1


count = 0

if n <= 0:
    print("Pleas enter a positive integer!")
elif n == 1 :
    print("Fibonacci sequence up to 1 number:")
    print(a)
else:
    print("Fibonacci sequence is ")
    while count < n:
        print(a ,end=" ")
        c = a+b
        a= b
        b = c
        count +=1


