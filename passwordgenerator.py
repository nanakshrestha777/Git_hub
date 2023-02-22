import random
import string

length = 10

charset = string.ascii_letters + string.digits + string.punctuation

password_list = random.choices(charset, k=length)
password = ''.join(password_list)
print(password)
# writing a file
with open("password.txt", "w") as fd:
    fd.write(password)
    
# reading a file
with open("password.txt", "r") as fd:
    password = fd.read()
    
    
