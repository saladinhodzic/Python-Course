# creating functions with outputs

def format_name(first,last):
    """This is example of docstring which can be used to
    give information about the function and can be written multi line"""
    if first=='' or last== '':
        return 'You entered invalid value'
    return f"{first} {last}".title()

print(format_name(input("enter first name"),input('enter last name')))