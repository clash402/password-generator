import random


# PROPERTIES
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# METHODS
def generate_random_chars(count, chars):
    return [random.choice(chars) for _ in range(count)]


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


# MAIN
print("Welcome to the PyPassword Generator")

char_count = int(input("How many characters would you like in your password?\n"))

letter_count = random.randint(0, char_count)
char_count -= letter_count
number_count = random.randint(0, char_count)
char_count -= number_count
symbol_count = char_count

password = generate_random_chars(letter_count, letters)
password.append(generate_random_chars(number_count, numbers))
password.append(generate_random_chars(symbol_count, symbols))
password = flatten_list(password)

random.shuffle(password)
password = ''.join(password)

print("Your new password is:")
print(password)
