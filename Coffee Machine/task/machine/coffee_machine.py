class CoffeeMachine:

    def __init__(self):
        self.cur_water = 550
        self.cur_milk = 400
        self.cur_coffee = 120
        self.cur_cups = 9
        self.cur_money = 550
        self.cur_state = 'Choosing an action'


    def espresso(self):
        if self.cur_water >= 250 and self.cur_coffee >= 16 and self.cur_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.cur_water -= 250
            self.cur_coffee -= 16
            self.cur_cups -= 1
            self.cur_money += 4
        else:
            if self.cur_water < 250:
                print('Sorry, not enough water!')
            if self.cur_coffee < 15:
                print('Sorry, not enough coffee beans!')
            if self.cur_cups < 1:
                print('Sorry, not enough disposable cups!')
        return self.cur_water, self.cur_coffee, self.cur_cups, self.cur_money


    def latte(self):
        if self.cur_water >= 350 and self.cur_milk >= 75 and self.cur_coffee >= 20 and self.cur_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.cur_water -= 350
            self.cur_milk -= 75
            self.cur_coffee -= 20
            self.cur_cups -= 1
            self.cur_money += 7
        else:
            if self.cur_water < 350:
                print('Sorry, not enough water!')
            if self.cur_milk < 75:
                print('Sorry, not enough milk!')
            if self.cur_coffee < 20:
                print('Sorry, not enough coffee beans!')
            if self.cur_cups < 1:
                print('Sorry, not enough disposable cups!')
        return self.cur_water, self.cur_milk, self.cur_coffee, self.cur_cups, self.cur_money


    def cappuccino(self):
        if self.cur_water >= 200 and self.cur_milk >= 100 and self.cur_coffee >= 12 and self.cur_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.cur_water -= 200
            self.cur_milk -= 100
            self.cur_coffee -= 12
            self.cur_cups -= 1
            self.cur_money += 6
        else:
            if self.cur_water < 200:
                print('Sorry, not enough water!')
            if self.cur_milk < 100:
                print('Sorry, not enough milk!')
            if self.cur_coffee < 12:
                print('Sorry, not enough coffee beans!')
            if self.cur_cups < 1:
                print('Sorry, not enough disposable cups!')
        return self.cur_water, self.cur_milk, self.cur_coffee, self.cur_cups, self.cur_money


    def buy(self):
        drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if drink == '1':
            self.espresso()
        elif drink == '2':
            self.latte()
        elif drink == '3':
            self.cappuccino()
        elif drink == 'back':
            pass



    def fill(self):
        self.cur_water += int(input('Write how many ml of water you want to add:'))
        self.cur_milk += int(input('Write how many ml of milk you want to add:'))
        self.cur_coffee += int(input('Write how many grams of coffee beans you want to add:'))
        self.cur_cups += int(input('Write how many disposable cups you want to add:'))
        return self.cur_water, self.cur_milk, self.cur_coffee, self.cur_cups, self.cur_money


    def take(self):
        print(f'I gave you ${self.cur_money}')
        self.cur_money = 0
        return self.cur_money


    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.cur_water} ml of water')
        print(f'{self.cur_milk} ml of milk')
        print(f'{self.cur_coffee} g of coffee beans')
        print(f'{self.cur_cups} disposable cups')
        print(f'${self.cur_money} of money')
        print()

    def main_menu(self):
        if self.cur_state == 'Choosing an action':
            print()
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                self.cur_state = 'Break'
                return self.cur_state

coffeemachine = CoffeeMachine()

while coffeemachine.cur_state == 'Choosing an action':
    coffeemachine.main_menu()
