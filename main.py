from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
choice = input(f"What would you like? ({item.get_items()}): ")

while(choice != "off"):
    if choice == "report":
        print(coffee.report())
        print(money.report())
    else:
        drink = item.find_drink(choice)
        price = 0
        for menu in item.menu:
            if choice == menu.name:
                price = menu.cost
        print(price)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(price):
                coffee.make_coffee(drink)
    choice = input(f"What would you like? ({item.get_items()}): ")



