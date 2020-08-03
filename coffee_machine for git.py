import sys

class CoffeeMachine:
    
    def __init__(self, milk, water, coffee_beans, money, dis_cups):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.dis_cups = dis_cups
        self.money = money
        self.coffee_type = None
        self.text = None

    def input_text(self):
        return input()
    
    def display_supplies(self):
        return f'''The coffee machine has: 
{str(self.water)} of water
{str(self.milk)} of milk
{str(self.coffee_beans)} of coffee_beans
{str(self.dis_cups)} of disposable cups
${str(self.money)} of money'''
    
    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    
        self.coffee_type = self.input_text()
    
        if self.coffee_type == str(1):
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.resource_check()
        
        elif self.coffee_type == str(2):
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
            self.resource_check()

        elif self.coffee_type == str(3):
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.resource_check()
        
        elif self.coffee_type == "back":
            self.coffee_machine()
        self.dis_cups -= 1
    
    def resource_check(self):
        if self.water > 0:
            if self.milk > 0:
                if self.coffee_beans > 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    self.add_water()
                    self.add_coffee_beans()
                    self.add_milk()
                    self.add_dis_cups()
                    self.add_money()
                    print("Sorry, not enough coffee_beans!")
            else:
                self.add_water()
                self.add_coffee_beans()
                self.add_milk()
                self.add_dis_cups()
                self.add_money()
                print("Sorry, not enough milk!")
        else:
            self.add_water()
            self.add_coffee_beans()
            self.add_milk()
            self.add_dis_cups()
            self.add_money()
            print("Sorry, not enough water!")
    
    def fill_supplies(self):
        print("Write how many ml of water do you want to add: ")
    
        water_added = int(self.input_text())
        self.water += water_added
        print("Write how many ml of milk do you want to add: ")
    
        milk_added = int(self.input_text())
        self.milk += milk_added
        print("Write how many grams of coffee beans do you want to add: ")
    
        coffee_beans_added = int(self.input_text())
        self.coffee_beans += coffee_beans_added
        print("Write how many disposable cups of coffee do you want to add: ")
        
        disposable_cups_added = int(input())
        self.dis_cups += disposable_cups_added
    
    def take_money(self):
        print("I gave you $" + str(self.money))
        self.money -= self.money
    
    def done(self):
        sys.exit()
    
    def add_water(self):
        if self.coffee_type == str(1):
            self.water += 250
        elif self.coffee_type == str(2):
            self.water += 350
        elif self.coffee_type == str(3):
            self.water += 200
    
    def add_milk(self):    
        if self.coffee_type == str(2):
            self.milk += 75
        elif self.coffee_type == str(3):
            self.milk += 100
    
    def add_coffee_beans(self):
        if self.coffee_type == str(1):
            self.coffee_beans += 16
        elif self.coffee_type == str(2):
            self.coffee_beans += 20
        elif self.coffee_type == str(3):
            self.coffee_beans += 12
    
    def add_dis_cups(self):
        self.dis_cups += 1
    
    def add_money(self):
        if self.coffee_type == str(1):
            self.money -= 4
        elif self.coffee_type == str(2):
            self.money -= 7
        elif self.coffee_type == str(3):
            self.money -= 6

    def coffee_machine(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit): ")
            self.order = self.input_text()
            if self.order == "buy":
                self.buy_coffee()
            elif self.order == "fill":
                self.fill_supplies()
            elif self.order == "take":
                self.take_money()
            elif self.order == "remaining":
                print(self.display_supplies())
            elif self.order == "exit":
                self.done()

kunle = CoffeeMachine(540, 400, 120, 550, 9)
kunle.coffee_machine()