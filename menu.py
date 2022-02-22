class MenuItem:
    """Models each Menu Item."""
    def __init__(self, number, name, water, milk, coffee, cost):
        self.number = number
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(number=1, name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(number=2, name="Long espresso", water=100, milk=0, coffee=18, cost=2),
            MenuItem(number=3, name="Latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(number=4, name="Cappuccino", water=250, milk=50, coffee=24, cost=3),
            MenuItem(number=8, name="Status report", water=0, milk=0, coffee=0, cost=0),
            MenuItem(number=9, name="Refill", water=0, milk=0, coffee=0, cost=0),
            MenuItem(number=0, name="Quit", water=0, milk=0, coffee=0, cost=0)
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = {}
        for item in self.menu:
            options[item.number] = [item.name, item.cost]
        return options

    def find_drink(self, order_number):
        """Searches the menu for a particular drink by number.
        Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.number == order_number:
                return item
