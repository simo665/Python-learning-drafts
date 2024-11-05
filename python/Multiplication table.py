import asyncio
import sys
import time

# Title
print("**** Welcome to the multiplication table!! ****")

# variables
num = input("Enter a number: ")  # Value input
result = 0  # Result of the multiplication
value = 0  # Save the user value as a float

# Check if the value is a number
while True:
    try:
        value = float(num)
        break
    except ValueError:
        num = input("Please Enter a number: ")

# Helper function to print text with a fade/typing effect
async def fade_text(text):
    for char in text:
        print(char, end='', flush=True)
        await asyncio.sleep(0.05)  # Delay for each character
    print()  # New line after text is printed

# Print the multiplications of the value for 1 to 10
async def multiply_table():
    for i in range(1, 11):
        result = int(num) * i
        await fade_text(f"{num} × {i} = {result}")
        await asyncio.sleep(0.2)

# Run the async function
asyncio.run(multiply_table())
