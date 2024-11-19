## Calculator 


# Steps:
	# 1. Welcome message 
	# 2. Make the operations functions 
	# 3. Get user input
	# 4. Calculate the result
	

# Addition 
def addition(numA, numB):
	Results = numA + numB
	return Results 
# Substraction 
def substraction(numA, numB):
	Results = numA - numB
	return Results 
# multiplication
def multiplication(numA, numB):
	Results = numA * numB
	return Results 
# division
def division(numA, numB):
	Results = numA / numB
	return Results 

def convert_to_int(variable):
	try:
		variable = int(variable )
		return variable
	except ValueError:
		print("Enter numbers!")
		return None

def main():
	while True:
		mark = input("Select the type of operation [+, -, ×, ÷]: ")
		num_a = input("First number: ")
		num_b = input("Second number: ")
		num_a = convert_to_int(num_a)
		num_b = convert_to_int(num_b)
		if mark == "+":
			result = addition(num_a, num_b)
			print(f"Result = {result}")
		elif mark == "-":
			result = substraction(num_a, num_b)
			print(f"Result = {result}")
		elif mark == "×":
			result = multiplication(num_a, num_b)
			print(f"Result = {result}")
		elif mark == "÷":
			result = division(num_a, num_b)
			print(f"Result = {result}")
		else:
			print("Please enter a valid operator!")

main()