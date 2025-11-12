# Define Global Variables
restaurant_name = "Hungry Hare"

menu = {
    "sku1": {
        "name": "Hamburger",
        "price": 6.51
    },
    "sku2": {
        "name": "Cheesebruger",
        "price": 7.75
    },
    "sku3": {
        "name": "Milshake",
        "price": 5.99
    },
    "sku4": {
        "name": "Fries",
        "price": 2.39
    },
    "sku5": {
        "name": "Sub",
        "price": 5.87
    },
    "sku6": {
        "name": "Ice Cream",
        "price": 1.55
    },
    "sku7": {
        "name": "Fountain Drink",
        "price": 3.45
    },
    "sku8": {
        "name": "Cookie",
        "price": 3.15
    },
    "sku9": {
        "name": "Brownie",
        "price": 2.46
    },
    "sku10": {
        "name": "Sauce",
        "price": 0.75
    }
}

# print(menu["sku1"][0])

app_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit",
}

sales_tax_rate = 0.07
cart = {}

# Displaying the menu - define several custom functions that handle the app actions
def display_menu():
    print("\n***** Here is the menu *****\n")
    for sku in menu:
        parsed_sku = sku[3:]
        item = menu[sku]['name']
        price = menu[sku]['price']
        print("(" + parsed_sku + ")" + " " + item + ": $" + str(price))
    print("\n")

def add_to_cart(parsed_sku, quantity=1):
    sku = "sku" + parsed_sku
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print("Added ", quantity, " of ", menu[sku]['name'], " to the cart.")
    else:
        print("I'm sorry. The menu number", sku, "that you entered is not on the menu.")

def remove_from_cart(parsed_sku):
    sku = "sku" + parsed_sku
    if sku in cart:
        cart.pop(sku)
        print(f"\nRemoved {menu[sku]['name']} from the cart.\n")
    else:
        print(f"I'm sorry. The item with SKU {sku} is not currently in the cart.")

def modify_cart(parsed_sku, quantity):
    sku = "sku" + parsed_sku
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print("Modified", menu[sku]['name'], "quantity to ", quantity, " in the cart.")
        else:
            remove_from_cart(sku)
    else:
        print(f"I'm sorry. The item with SKU {sku} is not currently in the cart.")

def view_cart():
    print("\n*****Cart Contents*****\n")
    subtotal = 0
    for sku in cart:
        if sku in menu:
            quantity = cart[sku]
            subtotal += menu[sku]["price"] * quantity
            print(f"{quantity} X {menu[sku]['name']}")
    tax = subtotal * sales_tax_rate
    subtotal += tax
    print(f"Total: ${round(subtotal, 2)}\n")

def checkout():
    print("\n*****Checkout*****\n")
    view_cart()
    print("Thank you for your order! Goodbye!\n")
    
def get_sku_and_quantity(sku_prompt, quantuty_prompt = None):
    item_sku = input(sku_prompt)
    if quantuty_prompt:
        quantity = input(quantuty_prompt)
        if not quantity.isdigit():
            quantity = 1
        quantity = int(quantity)
        return item_sku, quantity
    else:
        return item_sku
    
def order_loop():
    print(f"---------- Welcome to {restaurant_name} ---------")
    ordering = True
    while(ordering):
        print("\n***** Ordering Actions *****\n")
        for number in app_actions:
            description = app_actions[number]
            print("(" + number + ")", description)
        
        response = input("Please enter the number of the action you want to take: ")
        if response == '1':
            # User wants to order a menu item. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to order: "
            quantity_prompt = "Please enter the quantity you want to order [default is 1]: "
            ordered_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(ordered_sku, quantity)
        elif response == "2":
            # User wants to remove an item from the cart. Prompt them for SKU only.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to remove: "
            item_sku = get_sku_and_quantity(sku_prompt)
            remove_from_cart(item_sku)
        elif response == "3":
            # User wants to modify an item quantity in the cart. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to modify: "
            quantity_prompt = "Please enter the quantity you want to change to [default is 1]: "
            item_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_cart(item_sku, quantity)
        elif response == "4":
            # User wants to view the current cart contents. No user input needed.
            view_cart()
        elif response == "5":
            # User wants to checkout. No user input needed. Terminate the while loop after displaying.
            checkout()
            ordering = False
        elif response == "6":
            # User wants to exit before ordering. No user input needed. Terminate the while loop.
            print("Goodbye!")
            ordering = False
        else:
            # User has entered an invalid action number. Display a message.
            print("You have entered an invalid action number. Please try again.")

order_loop()
