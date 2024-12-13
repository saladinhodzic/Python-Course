# Object Oriented Programing

# from turtle import Turtle,Screen

# rafaelo=Turtle()
# rafaelo.shape("turtle")
# rafaelo.color("green")
# rafaelo.forward(50)
# Screen().exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Makarone",["Pesto", "Milano","Americana"])
table.add_column("Kafe",["Espresso", "Macchiato","Capuccino"])
table.align='l'
print(table)