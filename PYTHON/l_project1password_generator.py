import random
import string

def generate_password(len):
  char = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(char) for i in range(len))
  return password
  
password_length = int(input("Enter Desired Passwd Length: "))
generated_password = generate_password(password_length)

print("Generated Password: ", generated_password)
  