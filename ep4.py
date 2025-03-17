beard_length = 1

print(" Hello, thank you for coming in to Roberto's coffee shop!")

customer_name = input("What is your name?\n")

beard_existent = (input(f"{customer_name}, do you have a beard?"))

if beard_existent == "no":
    print("Please grow a beard and return later! ")
    exit()
else:
    beard_length = float(input("How long is your beard in inch? "))
    if beard_length >= 1:
        print("Well, great beard! You can skip ahead the line?. ")
        exit()
    else:
        print("You have to wait in line!")
        exit()




