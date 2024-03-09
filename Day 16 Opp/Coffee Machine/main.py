from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

run = True

def start():
    global run
    menuobj = Menu()
    print("Welcome to the coffee machine")
    print("What would you like to have?" + menuobj.get_items())
    choice = input().strip().lower()
    print(choice)

    if choice == "off":
        run = False
        print("Bye!")
    elif choice == "report":
        CoffeeMaker.report()

while (run):
    start()
