import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
numb_letters = int(input(f"How many letters do you want in your password?\n"))
numb_numbers = int(input(f"How many many numbers do you want in your password\n"))
numb_symbols = int(input(f"How many symbols do you want in your password?\n"))

# Add the alphanumericsymbol to a list
password = []
for letter in range(1, numb_letters + 1):
    password.append(random.choice(letters))
for number in range(1, numb_numbers + 1):
    password.append(random.choice(numbers))
for symbol in range(1, numb_symbols + 1):
    password.append(random.choice(symbols))

# random.shuffle is used to shuffle a list
random.shuffle(password)
# print(password)

# convert the password list to a string
new_password = ""
for char in password:
    new_password += char
print(new_password)