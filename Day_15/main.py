from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_maschine = MoneyMachine()
kaffee_macher = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    optionen = menu.get_items()
    wahl= input(f"Was möchten Sie? ({optionen}) ")
    if wahl == "off":
        is_on = False
    elif wahl == "report":
        kaffee_macher.report()
        money_maschine.report()
    else:
        getrank = menu.find_drink(wahl)
        if kaffee_macher.is_resource_sufficient(getrank) and money_maschine.make_payment(getrank.cost):
            kaffee_macher.make_coffee(getrank)
                
                
        