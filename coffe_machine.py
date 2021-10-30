# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:37:23 2021

@author: Cyberpunk
"""

# cofffee-machine
#OOP concept implemented.
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def buy(self):
        coffe = input("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
""")
        if coffe == "back":
            return
        elif coffe == "1" and self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
            print("")
            return
        elif coffe == "1" and self.water < 250:
            print("Sorry, not enough water!")
            print("")
            return
        elif coffe == "1" and self.coffee_beans < 16:
            print("Sorry, not enough coffee beans!")
            print("")
            return
        elif coffe == "1" and self.cups < 1:
            print("Sorry, not enough disposable cups!")
            print("")
            return
        elif coffe == "2" and self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")
            print("")
            return
        elif coffe == "2" and self.water < 350:
            print("Sorry, not enough water!")
            print("")
            return
        elif coffe == "2" and self.milk < 75:
            print("Sorry, not enough milk!")
            print("")
            return
        elif coffe == "2" and self.coffee_beans < 20:
            print("Sorry, not enough coffee beans!")
            print("")
            return
        elif coffe == "2" and self.cups < 1:
            print("Sorry, not enough disposable cups!")
            print("")
            return
        elif coffe == "3" and self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")
            print("")
            return
        elif coffe == "3" and self.water < 200:
            print("Sorry, not enough water!")
            print("")
            return
        elif coffe == "3" and self.milk < 100:
            print("Sorry, not enough milk!")
            print("")
            return
        elif coffe == "3" and self.coffee_beans < 12:
            print("Sorry, not enough coffee beans!")
            print("")
            return
        elif coffe == "3" and self.cups < 1:
            print("Sorry, not enough disposable cups!")
            print("")
            return
        elif coffe != "1" or "2" or "3":
            print("Enter correct option! : 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            return self.buy()

    def fill(self):
        a = int(input("""Write how many ml of water do you want to add:
"""))
        b = int(input("""Write how many ml of milk do you want to add:
"""))
        c = int(input(""""Write how many grams of coffee beans do you want to add:
"""))
        d = int(input("""Write how many disposable cups of coffee do you want to add:
"""))
        self.water += a
        self.milk += b
        self.coffee_beans += c
        self.cups += d
        print("")
        return

    def take(self):
        print("")
        print(f'I gave you ${self.money}')
        self.money -= self.money
        print("")
        return

    def remaining(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money")
        return

coffee = CoffeeMachine()

while True:
    act = input("""Write action (buy, fill, take, remaining, exit):
""")
    if act == "buy":
        coffee.buy()
    elif act == "fill":
        coffee.fill()
    elif act == "take":
        coffee.take()
    elif act == "remaining":
        coffee.remaining()
    elif act == "exit":
        break
    else:
        print("Enter correct option! : (buy, fill, take, remaining, exit)")
