from data import MENU,resources

# TODO - ask user for coffee


def ask_for_drink():
    return input("What would you like? (espresso/latte/cappuccino): ")

is_off=False
# TODO - on saying word 'off' it should end the program

order=ask_for_drink()
while is_off==False:
    if order =='off':
        print("Have a nice day!")
        is_off=True
    elif order == 'report':
        print(resources)
        order=ask_for_drink()



# TODO - on saying word 'report' it should print the coffee machine current resources


# TODO - check if coffee machine has enough resources for making the user coffee


# TODO - If it has enough resources then it should ask for coins (penny, dimes, nickel, quarters)

# TODO - Check if user inserted enough money, if it has too much money then it should refund

# TODO - Deduce the resources from coffe machine and wish the user happy day