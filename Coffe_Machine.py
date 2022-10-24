MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def water(cofe):
    fuck = MENU[cofe]["ingredients"]["water"]
    return fuck
def dashla2(cofe):
    w = MENU[cofe]["ingredients"]["water"]
    c = MENU[cofe]["ingredients"]["coffee"]
    cos = MENU[cofe]["cost"]
    resources["water"] -= w
    resources["coffee"] -= c
    resources["money"] += cos
    return f"{cos}"
def dashla(cofe):
    w = MENU[cofe]["ingredients"]["water"]
    m = MENU[cofe]["ingredients"]["milk"]
    c = MENU[cofe]["ingredients"]["coffee"]
    cos = MENU[cofe]["cost"]
    resources["water"] -= w
    resources["milk"] -= m
    resources["coffee"] -= c
    resources["money"] += cos
    return f"{cos}"
def report(res):
    water = res["water"]
    milk = res["milk"]
    cofe = res["coffee"]
    money = res["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {cofe}gm")
    print(f"Money: {money}$")
def coins(q, d, n, p):
    qq = q * 0.25
    dd = d * 0.10
    nn = n * 0.05
    pp = p * 0.01
    return f"{round(qq + dd + nn + pp, 2)}"
def coin(a):
    return MENU[a]["cost"]
game = True
while game:
    ask = input("What would you like? (latte/cappuccino/espresso): ")
    if ask == "report":
        report(resources)
        continue
    elif ask == "off":
        game = False
    elif ask == "espresso":
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penies = int(input("How many pennies?: "))
        cots = coins(quarter, dime, nickle, penies)
        if float(cots) < float(coin(ask)):
            print("Sorry there is not enough money!")
            continue
        if resources["water"] < water(ask):
                print("There is no enough water!")
                continue
        else:
            print(f"Here is {float(cots) - float(dashla2(ask))}$ in change")
            print(f"Here is your {ask} Enjoy")
    elif ask == "latte":
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penies = int(input("How many pennies?: "))
        cots = coins(quarter, dime, nickle, penies)
        if float(cots) < float(coin(ask)):
            print("Sorry there is not enough money!")
            continue
        if resources["water"] < water(ask):
                print("There is no enough water!")
                continue
        else:
            print(f"Here is {float(cots) - float(dashla(ask))}$ in change")
            print(f"Here is your {ask} Enjoy")
    elif ask == "cappuccino":
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penies = int(input("How many pennies?: "))
        cots = coins(quarter, dime, nickle, penies)
        if float(cots) < float(coin(ask)):
            print("Sorry there is not enough money!")
            continue
        if resources["water"] < water(ask):
                print("There is no enough water!")
                continue
        else:
            print(f"Here is {float(cots) - float(dashla(ask))}$ in change")
            print(f"Here is your {ask} Enjoy")
    else:
        print("Please enter coffe type!")

