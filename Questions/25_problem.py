# 25. Guess the number game (fixed number).
import random
n = int(input("enter a number: "))
game = random.ra(1,100)


if n == game:
    print("Won")
else:
    print("lose")

print(game)