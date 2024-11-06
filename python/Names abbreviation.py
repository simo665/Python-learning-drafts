friends_list = input("Enter your friends first and last name sperated by a comma: ").split(", ")

shortcuts_list = []

for friend in friends_list:
    friend_name = friend.split()
    print(friend_name)
    
    first_name = friend_name[0][0]
    last_name = friend_name[1][0]
    shortcut = f"{first_name}.{last_name}.".upper()
    shortcuts_list.append(shortcut)
    
print("\nAbbreviated names:\n")
for shortcut in shortcuts_list:
	print(f" => {shortcut}")