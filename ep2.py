#Variables in python

#Let's start a coffee shop together!! We're going to buidl a cofee shop using some new Python programming concepts!!

#Lets's build a robot barista


print("Hello welcome to Roberto's cofee shop!!!")

costumer_name = input("What is your name? \n")

print(f"Hello, {costumer_name}, I will be your barista, thank you for coming in today. \n\n\n")

menu = "Black Coffe , Espresso, Latte, Cappucino"

print(f" {costumer_name}, here is our menu:\n {menu}")

print("What would you like from our menu? ")

order = input()

price = 8

quantity = int(input("How many coffees would you like?\n"))

total = price * quantity

print(f"It is going to be {quantity} {order}. Your total is: ${total}, and it will be ready in 5 minute.")




