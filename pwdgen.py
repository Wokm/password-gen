#import random and string modules to use their features.
import random
import string

#function that generates a 10 character password using a
# random combination of letters, numbers, and special characters.
def generate_password(length=10):
    letters= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

#stores the generated password in a variable and prints it.
password=generate_password()
print("Generated password:", password)

