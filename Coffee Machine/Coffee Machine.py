water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) + " of coffee beans")
    print(str(disposable_cups) + " of disposable cups")
    print("$" + str(money) + " of money")


def buy():
    global water, beans, milk, money, disposable_cups
    choice = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))

    if choice == "1":
        if water >= 250 and beans >= 16:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            money += 4
            disposable_cups -= 1
        elif water < 250:
            print("Sorry, not enough water!")
        elif beans < 16:
            print("Sorry, not enough coffee beans!")
    elif choice == "2":
        if water >= 350 and milk >= 75 and beans >= 20:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            disposable_cups -= 1
        elif water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif beans < 20:
            print("Sorry, not enough coffee beans!")
    elif choice == "3":
        if water >= 200 and milk >= 100 and beans >= 12:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            disposable_cups -= 1
        elif water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif beans < 12:
            print("Sorry, not enough coffee beans!")
    elif choice == "back":
        pass


def fill():
    global water, milk, beans, disposable_cups
    new_water = int(input("Write how many ml of water do you want to add:"))
    new_milk = int(input("Write how many ml of milk do you want to add:"))
    new_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    new_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))

    water += new_water
    milk += new_milk
    beans += new_beans
    disposable_cups += new_disposable_cups

    print()


def take():
    global money
    print("I gave you $" + str(money))
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "exit":
        break
    elif action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    print()
