# creating functions with outputs

def format_name(first,last):
    if first=='' or last== '':
        return 'You entered invalid value'
    return f"{first} {last}".title()

print(format_name(input("enter first name"),input('enter last name')))