# 37. Number guessing game with random number 1–50 and hints.
import random
#kya hum for loop ko is me use nhi karsakte ma ne jab for loop ko use kia to os me int ka masla a rah tha
player = int(input("Guess the number: "))
computer = random.randint (1,100)
print(computer)
while player!=computer :
    if computer>player:
        print("Try greater")
    elif computer<player:
        print("Try smaller")
    
    user = int(input("Guess the number: "))
    
print(f"You won the number was {computer}")