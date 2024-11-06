friends_list = input("Enter your friends first and last name sperated by a comma: ")

friends_list = friends_list.split(", ")
shortcuts_list = []

for friend in friends_list:
    friend_name = friend.split()
    print(friend_name)
    
    f1 = friend_name[0][0]
    f2 = friend_name[1][0]
    shortcut = f"{f1}.{f2}.".upper()
    shortcuts_list.append(shortcut)
    
print("\nAbbreviated names:\n")
for shortcut in shortcuts_list:
	print(f" => {shortcut}")