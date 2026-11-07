import string
import secrets

length = int(input("Desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(secrets.choice(characters) for i in range(length))
print("Auto-generated password: " + password)