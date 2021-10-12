# Caitlyn Rogers
# CSCI 1200A
# Lab Exercise 7.1
# 10/4/21
# lab_7_1.py

responses = {}
polling_active = True
additional_input = True
correct_input = True
choices = ['YES', 'NO']

print("Welcome to Python Travel! \nThank you for participating in the 2019 Spring Break poll.")
print("--------------------------------")
while polling_active:
	
	
	while additional_input:
		user_name = input("\nWhat is your name? ")
		user_choice = input(f"\nHello, {user_name.title()}! Where would you like to go for Spring Break? ")
		while correct_input:
			user_verification = input(f"\n{user_name.title()} wants to go to {user_choice.title()}. Is this correct? (yes/no) ")
			if user_verification.upper() in choices:
				if user_verification.upper() == 'YES':
					print("\nThank you.")
					additional_input = False
					break
				else:
					print("\nLet's try that again.")
					break
			else:
				print("\nInvalid input. Please type yes or no.")
				continue
		
		responses[user_name] = user_choice 
		
	while True:
		user_input = input("\nAre there any other inputs? (yes/no) ")
		if user_input.upper() in choices:
			if user_input.upper() == 'NO':
				print("\nThank you for your responses.")
				polling_active = False
				additional_input = False
				break
			else:
				print("\nOkay.")
				additional_input = True
				break			
		else:
			print("\nInvalid input. Please type yes or no.")
	
	
			
print()
		
print(f"\n----Spring Break 2019 Poll----")

for user_name, user_choice in responses.items():
	print(f"\n{user_name.title()} wants to go to {user_choice.title()}.")
		
print("\n-----------End Poll-----------")

print()

print(f"\nThe responses dictionary: {responses}")


