text = input("Enter a text: ").split()
print("Reversed sentence: ", end="")
reverse_sentences = " ".join(text[::-1])
print(reverse_sentences)