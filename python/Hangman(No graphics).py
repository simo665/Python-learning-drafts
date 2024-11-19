import random

# Hangman game steps
# 1. Welcome the user
# 2. Make a list of words
# 3. Choose a random word from the list
# 4. Display the word with underscores
# 5. Ask the user to guess a letter
# 6. Check if the letter is in the word
# 7. If the letter is in the word, update the display
# 8. If the letter is not in the word, lower point by 1
# 9. If the user has no points left, game over
# 10. If the user has guessed all the letters, they win

# words list
print("    **** Welcome To Hangman Game ****")
words = ["apple", "orange", "lemon", "watermelon"]
point = 5
# get a random word
random_word = random.choice(words)
underscore = []

# replace letters with underscore 
for letter in random_word:
    underscore.append("_")

print(" ".join(underscore))

# Replace the the underscore with the correct user input 

while True:
    if "".join(underscore).lower() == random_word.lower():
        print("    **** You Won ****")
        break
    if point <= 0:
        print(f"The word was {random_word}")
        print("    **** You Lost ****")
        break
    guess = input("guss the letter: ")
    if guess not in random_word:
        point -= 1
        print(f"Wrong letter, still have {point} chances!")
    for position in range(len(random_word)):
        if guess.lower() == random_word[position].lower():
            if underscore[position].lower() != random_word[position].lower():
                underscore[position] = random_word[position]
                break 
            
                
    print("".join(underscore))