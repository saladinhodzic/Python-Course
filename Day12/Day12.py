# Scopes

# to modify the global scope variable you can call the global keyword inside the function
# but its best to avoid using that

enemies=1

def increase_enemies(enemies):
#     global enemies
    return enemies +1

# best practice is to pass it as argument and then save it into the variable

enemies+=increase_enemies(enemies)