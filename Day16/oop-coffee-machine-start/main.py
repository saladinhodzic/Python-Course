from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
is_true=True
while is_true:
    choice=input(f"Enter value:({menu.get_items()})")
    if choice=='off':
        is_true=False
    elif choice == 'report':
        coffee_maker.report()
    else:
        coffee=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)