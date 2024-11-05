import asyncio

## Title
async def TextAnim(text):
	for char in text:
		print(char, end="", flush=True)
		await asyncio.sleep(0.05)
	await ishop()

async def Title():				
	await TextAnim("              **** ISHOP CALCULATOR ****\n\n")
	
async def ishop():
	items_num = input("How many items do you want to buy? : ")
	items_list= []
	items_price= []
	while True:
		try:
			items_num = int(items_num)
			break
		except ValueError:
			items = input("Error, Please Enter a number of how many items: ")
	while not items_num > 0:
		print("you can't buy nothing.. try again.")
		items_num = input("How many items do you want to buy? : ")
		while True:
			try:
				items_num = int(items_num)
				break
			except ValueError:
				items = input("Error, Please Enter a number of how many items: ")
			
	for i in range(1, items_num + 1):
			item = input(f"enter item number {i} name: ")
			items_list.append(item)
			price = float(input(f"enter item number {i} price: $"))
			while True:
				try: 
					price = float(price)
					break 
				except ValueError:
					price = input("Error, Please Enter a number for the price: $")
			items_price.append(price)
	while True:
		option = input("Type 1 for items name, 2 for items total price, and 0 to close : ")
		while True:
			try:
				option= int(option)
				break 
			except ValueError:
				option = input("Type 1 for items name, 2 for items total price, and 0 to close (enter a number please) : ")
		if option == 1:
			print(items_list)
		elif option == 2:
			print(f"${sum(items_price):.2f}")
		elif option == 0:
			break 
		else:
			print("Your value doesn't match the options had given.")
			


asyncio.run(Title())
