from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
available_choices = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
print()



print(
"""
==========================
Welcome to COFFEE MACHINE!
==========================
""")

program_running = True

while program_running:

	print("""
	
Make your choice!
	""")

	for choice in available_choices:
		if choice in range(1, 5):
			print("{}: {} ${:.2f}".format(choice, available_choices[choice][0], available_choices[choice][1]))
	print()
	for choice in available_choices:
		if choice >= 8 or choice == 0:
			print("{}: {}".format(choice, available_choices[choice][0]))

	user_input = input("\nPlease, enter a number: ")
	while not user_input.isnumeric() or int(user_input) not in available_choices:
		user_input = input("Invalid input. Please, enter a number: ")

	if user_input == "0":
		print("\nThank you for using COFFEE MACHINE!")
		program_running = False
	elif user_input == "8":
		coffee_maker.report()
		money_machine.report()
	elif user_input == "9":
		coffee_maker.refill()
		money_machine.refill()
		print("\nCoffee machine refilled!")
		coffee_maker.report()
		money_machine.report()
	elif int(user_input) in range(1, 5):
		menu_item = menu.find_drink(int(user_input))
		if coffee_maker.is_resource_sufficient(menu_item):
			if money_machine.payment_sufficient(menu_item.cost):
				if money_machine.change_refund_possible(menu_item.cost):
					coffee_maker.make_drink(menu_item)
				else:
					print()
					print("Change refund not possible. Refill with coins!")


