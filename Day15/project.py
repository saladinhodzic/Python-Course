from data import MENU,resources

# TODO - ask user for coffee


def ask_for_drink():
    return input("What would you like? (espresso/latte/cappuccino): ")

is_off=False
# TODO - on saying word 'off' it should end the program

def check_resources(resources,user_coffee):
        if resources['water'] < user_coffee['ingredients']['water']:
            print("There is not enough water in machine!")
        elif resources['coffee'] < user_coffee['ingredients']['coffee']:
            print("There is not enough coffee in machine!")
        elif order=='espresso':
            print("Espresso is on the way!")
            return
        elif resources['milk'] < user_coffee['ingredients']['milk']:
            print("There is not enough milk in machine!")
        else:
            print(f"{order.title()} is on the way!")
            return
def enter_coins():
    pennys=int(input("Enter how much pennys"))
    nickels=int(input("Enter how much nickels"))
    dimes=int(input("Enter how much dimes"))
    quarters=int(input("Enter how much quarters"))
    return [pennys,nickels,dimes,quarters]

order=ask_for_drink()
while is_off==False:
    if order =='off':
        print("Have a nice day!")
        is_off=True
    elif order == 'report':
        print(resources)
        order=ask_for_drink()
    elif order == 'espresso':
        check_resources(resources,MENU['espresso'])
        coins=enter_coins()
        print(coins)
    
    elif order == 'cappuccino':
        check_resources(resources,MENU['cappuccino'])
        enter_coins()
    elif order == 'latte':
        check_resources(resources,MENU['cappuccino'])
        enter_coins()



# TODO - on saying word 'report' it should print the coffee machine current resources


# TODO - check if coffee machine has enough resources for making the user coffee


# TODO - If it has enough resources then it should ask for coins (penny, dimes, nickel, quarters)

# TODO - Check if user inserted enough money, if it has too much money then it should refund

# TODO - Deduce the resources from coffe machine and wish the user happy day