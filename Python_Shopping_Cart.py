#1) Takes in an input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, prints out a receipt of the items with total and quantity

def shopping_cart():
    list = {}
    total = []
    print("Welcome to your virtual shopping cart! Your cart is currently empty.")
    while True:
        ask = input("What would you like to do? (Add/Remove/Show/Clear/Quit)")
        if ask == "Add":
            item = input("What would you like to add?")
            quantity = input(f"How many {item}'s do you want to add?")
            cost = float(input(f"How much does a {item} cost?"))
            final_cost  = (float(cost) * int(quantity))
            total.append(final_cost)
            list[item] = (int(quantity), cost)
            if int(quantity) > 1:
                print(f"{quantity} {item}'s have been added to your cart.")
            if int(quantity) == 1:
                print(f"{quantity} {item} has been added to your cart.")
        elif ask == "Remove":
            remove = input("What item do you want to remove?")
            remove_quantity = input(f"How many {remove}'s do you want to remove?")
            list[remove] = (list[remove][0] - int(remove_quantity), list[remove][1])
            if int(quantity) > 1:
                print(f"{quantity} {item}'s have been removed to your cart.")
            if int(quantity) == 1:
                print(f"{quantity} {item} has been removed to your cart.")
        elif ask == "Show":
            print("Here is your shopping cart:")
            for item, (quantity,cost) in list.items():
                print(f"{quantity} {item} x ${cost}")
        elif ask == "Clear":
            check = input("Are you sure you want to clear your shopping cart? This action cannot be undone. (Y/N)")
            if check == "Y":
                list.clear()
                print("Your shopping cart has been emptied.")
        elif ask == "Quit":
            quit = input("Are you sure you want to quit? (Y/N)")
            if quit == "Y":
                print("Here is your shopping cart receipt:")
                for item, (quantity,cost) in list.items():
                    print(f"{quantity} {item} x ${cost}")
                print(f"Your total is " "$" + str(round(sum(total),2)))
                break
        else:
            print("invalid entry, please try again.")

shopping_cart()




