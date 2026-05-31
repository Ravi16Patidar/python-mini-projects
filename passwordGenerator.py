import random
password_length=0
while True:
    try:
        password_length=int(input("Enter password length\n"))
        break;
    except ValueError:
        print("Enter valid number")
        continue

def passwordGenerator(password_chars):
    # global password
    password=""
    for _ in range(password_length):
        randomNumber=random.randint(0, len(password_chars)-1)
        password+=password_chars[randomNumber]
    return password

passwordLevel=input("Enter which level of password you want e.g low, high, medium\n").lower()

match passwordLevel:
    case "low":
        password_chars="0123456789abcdefghijklmnopqrstuvwxyz"
        print(passwordGenerator(password_chars))
        
    case "medium":
        password_chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        print(passwordGenerator(password_chars))
    case "high":
        password_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"
        print(passwordGenerator(password_chars))
    case _:
        print("Please enter only low,medium ,high")

