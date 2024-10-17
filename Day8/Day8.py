def greet (name):
    print(name)

greet("Saladin")

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How is it in {location}")

# positional arguments
greet_with('saladin','novi pazar')
# keyword arguments
greet_with(location="Novi pazar",name="saki")