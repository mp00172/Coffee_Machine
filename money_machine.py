class MoneyMachine:

	CURRENCY = "$"

	COIN_VALUES = {
		"quarters": 0.25,
		"dimes": 0.10,
		"nickles": 0.05,
		"pennies": 0.01
	}

	def __init__(self):
		self.coins_containing = {
			"quarters": 5,
			"dimes": 5,
			"nickles": 10,
			"pennies": 10
		}

		self.coins_inserted = {
			"quarters": 0,
			"dimes": 0,
			"nickles": 0,
			"pennies": 0
		}
		self.summ_inserted = 0

		self.coins_to_return = {
			"quarters": 0,
			"dimes": 0,
			"nickles": 0,
			"pennies": 0
		}
		self.summ_to_return = 0

########################################################################################################################

	def summ_containing(self):
		"""Returns summ of containing coins."""
		summ_containing = 0
		for coin in self.coins_containing:
			summ_containing += self.coins_containing[coin] * self.COIN_VALUES[coin]
		summ_containing = round(summ_containing, 2)
		return summ_containing

	def clear_coins_inserted(self):
		"""Clears coins_inserted dict and summ."""
		self.coins_inserted = {
			"quarters": 0,
			"dimes": 0,
			"nickles": 0,
			"pennies": 0
		}
		self.summ_inserted = 0

	def clear_coins_to_return(self):
		"""Clears coins_to_return dict and summ."""
		self.coins_to_return = {
			"quarters": 0,
			"dimes": 0,
			"nickles": 0,
			"pennies": 0
		}
		self.summ_to_return = 0

	def coins_from_inserted_to_containing(self):
		"""Moves coins from "inserted" to "containing" dict."""
		for i in self.COIN_VALUES:
			self.coins_containing[i] += self.coins_inserted[i]
		self.clear_coins_inserted()

	def report(self):
		"""Prints containing coin amount"""
		for contaning_coin in self.coins_containing:
			print(f"{contaning_coin}: {self.coins_containing[contaning_coin]}")
		print("Summ containing: {}{:.2f}".format(self.CURRENCY, self.summ_containing()))

	def receive_coins(self):
		"""Receives coins, puts them in coins_inserted and coins_containing dict, and calculates the summ."""
		print("\n\nPlease insert coins.")
		for coin in self.COIN_VALUES:
			inserted_coin = input(f"How many {coin} ({self.CURRENCY}{self.COIN_VALUES[coin]})?: ")
			while not inserted_coin.isnumeric():
				inserted_coin = input(f"Invalid input. How many {coin} ({self.CURRENCY}{self.COIN_VALUES[coin]})?: ")
			self.coins_inserted[coin] = int(inserted_coin)
			self.summ_inserted += self.COIN_VALUES[coin] * int(inserted_coin)
		print("Summ inserted: {}{:.2f}".format(self.CURRENCY, self.summ_inserted))

	def payment_sufficient(self, drink_cost):
		"""Returns True when payment is sufficient, or False if insufficient."""
		self.receive_coins()
		if self.summ_inserted >= drink_cost:
			return True
		else:
			print("Not enough money!")
			self.print_refund(self.coins_inserted)
			self.clear_coins_inserted()
			return False

	def calculate_change(self, drink_price, amount_inserted):
		"""Returns change amount."""
		summ_to_return = amount_inserted - drink_price
		summ_to_return = round(summ_to_return, 2)
		return summ_to_return

	def change_refund_possible(self, drink_cost):
		"""Checks if the machine can return the change.
		Returns True or False."""
		summ_to_return = self.calculate_change(drink_price=drink_cost, amount_inserted=self.summ_inserted)
		if summ_to_return == 0:
			self.coins_from_inserted_to_containing()
			self.clear_coins_inserted()
			self.clear_coins_to_return()
			return True
		for i in self.COIN_VALUES:
			while summ_to_return >= self.COIN_VALUES[i]:
				if self.coins_inserted[i] >= 1:
					self.coins_inserted[i] -= 1
					self.coins_to_return[i] += 1
					summ_to_return -= self.COIN_VALUES[i]
					summ_to_return = round(summ_to_return, 2)
				else:
					break
			while summ_to_return >= self.COIN_VALUES[i]:
				if self.coins_containing[i] >= 1:
					self.coins_containing[i] -= 1
					self.coins_to_return[i] += 1
					summ_to_return -= self.COIN_VALUES[i]
					summ_to_return = round(summ_to_return, 2)
				else:
					break
			if summ_to_return == 0:
				self.print_refund(self.coins_to_return)
				self.coins_from_inserted_to_containing()
				self.clear_coins_inserted()
				self.clear_coins_to_return()
				return True

	def print_refund(self, dict_to_print):
		"""Prints out the refund."""
		refund = 0
		print("\n\nHere is your refund:")
		for i in dict_to_print:
			if dict_to_print[i] >= 1:
				refund += dict_to_print[i] * self.COIN_VALUES[i]
				refund = round(refund, 2)
				print("{} {}".format(dict_to_print[i], i))
		print("Summ = ${:.2f}".format(refund))

	def refill(self):
		"""Refills the coins_containing dict."""
		self.coins_containing["quarters"] += 5
		self.coins_containing["dimes"] += 5
		self.coins_containing["nickles"] += 10
		self.coins_containing["pennies"] += 10


#####################################################################################################


