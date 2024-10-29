# Scopes

# to modify the global scope variable you can call the global keyword inside the function
# but its best to avoid using that

enemies=1

def increase_enemies():
    global enemies
    enemies+=1
