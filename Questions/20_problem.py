# 19. Simple password check (fixed password).
user = input("Enter password: ")
password = "rehman"

for i in user:
    if i in password:
        print("Access Granted")
        break
    else:
        print("Access denied")