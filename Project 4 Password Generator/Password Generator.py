import random
import string

print("**Password Generator**")

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter Password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your String Password: ", password)