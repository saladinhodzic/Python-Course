# Requisition Project using Python
from datetime import datetime,timedelta
date = str(datetime.now().date() + timedelta(days=1))
month = date.split("-")[1]
day = date.split("-")[2]

pattern = f"PRM-{day}{month}-ODR290\n"

articles = {}

def add_articles(local):
    if local not in articles:
        articles[local] = {}
    while True:
        need = input(f"What do you need for {local}: ").title()
        if need == '':
            break
        quantity = input(f"How much of {need} you need: ")
        articles[local][need] = quantity
    
for _ in range(3):
    local = input("Enter the local name: ").title()
    if local:
        add_articles(local)

for key,items in articles.items():
    pattern += f"\n{key}:\n"
    
    for item,quantity in items.items():
        pattern += f" {quantity} {item}\n"

with open("premija.txt",'w') as file:
    file.write(pattern)