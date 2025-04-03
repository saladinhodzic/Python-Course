# Requisition Project using Python
from datetime import datetime
date = str(datetime.now().date())
month = date.split("-")[1]
day = date.split("-")[2]

pattern = f"PRM-{day}{month}-ODR290\n"

articles = {}

def add_articles(local):
    needs = input(f"What do you need for {local}: ").title()
    if needs:
        if local not in articles.keys():
            quantity = input(f"How much of {needs} you need: ")
            articles[local] = {needs:quantity}
            return add_articles(local)
        quantity = input(f"How much of {needs} you else need: ")
        articles[local].update({needs:quantity})
        return add_articles(local)
for _ in range(2):
    local = input("Enter the local name: ").title()
    add_articles(local)
    pattern += f"{local}:\n"
    for item,quantity in articles[local].items():
        pattern+=f"{quantity}x {item}\n"

print(pattern)