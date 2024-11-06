import random 
import string 

password_lenght = 0
letters_num = 0
numbers_num = 0
symbols_num = 0

pass_requirements = []

while True:
	password_lenght = int(input("\nEnter the total of characters in the password: "))
	letters_num = int(input("\nHow many letters you want in the password? : "))
	numbers_num = int(input("\nHow many numbers you want in the password? : "))
	symbols_num = int(input("\nHow many symbols you want in the password? : "))
	
	if (letters_num + numbers_num + symbols_num) != password_lenght:
		print("\nInvalid input, the sum of latters, numbers, symbols. doesn't match the password total characters. try again")
	else:
		break 
		
random_letter = random.choices(string.ascii_letters, k=letters_num)
random_number = random.choices(string.digits, k=numbers_num)
random_symbols = random.choices(string.punctuation, k=symbols_num)

pass_requirements = (random_letter + random_number + random_symbols)
random.shuffle(pass_requirements)

password = "".join(pass_requirements)

print(f"Generated password: {password}")
		