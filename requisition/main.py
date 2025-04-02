# Requisition Project using Python
from datetime import datetime
date = str(datetime.now().date())
month = date.split("-")[1]
day = date.split("-")[2]

pattern = f"PRM-{day}{month}-ODR290"

articles = {}    

def add_articles(local):
    needs = input(f"What do you need for {local}: ")
    if needs:
        if local.title() not in articles.keys():
            quantity = input(f"How much of {needs} you need: ")
            articles[local.title()] = {needs:quantity}
            return add_articles(local)
        quantity = input(f"How much of {needs} you else need: ")
        articles[local.title()].update({needs:quantity})
        return add_articles(local)
for _ in range(2):
    local = input("Enter the local name: ")
    add_articles(local)
print(articles)