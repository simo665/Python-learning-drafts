text = input("Enter a text: ")
text_list = text.split()
reverse_txt = []
for word in text_list[::-1]:
	reverse_txt.append(word)
print(text_list)
print(reverse_txt)