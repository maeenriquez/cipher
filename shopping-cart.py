cart = []

# Main function of the program
def main():
    print("Welcome to your shopping cart!")
    print("Please enter any of the following number:")
    print("1: add an item")
    print("2: remove an item")
    print("3: update an item")
    print("4: view cart")
    print("5: exit program")
    while True:
        try:
            action = int(input("What would you like to do? "))
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if action == 1:
                product, price, quantity = validate_input(action)
                add_item(product, price, quantity)
            elif action == 2:
                product = validate_input(action)
                remove_item(product)
            elif action == 3:
                product, quantity = validate_input(action)
                update_quantity(product, quantity)
            elif action == 4:
                view_cart()
            elif action == 5:
                break
            else:
                print("Invalid input. Please try again.")


# Validates the user input, especially when the price and quantity inputted are not numeric 
def validate_input(action):
    product = input("Enter the product: ")
    if action == 1:
        try:
            price = float(input(f"Enter the price of {product}: "))
            quantity = float(input(f"Enter quantity of {product}: "))
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            return product, price, quantity
    elif action == 2:
        return product
    elif action == 3:
        try:
            quantity = float(input(f"Enter updated quantity of {product}: "))
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            return product, quantity


# Adds an item to the shopping cart
def add_item(product, price, quantity):
    global cart
    product = product.lower()
    for row in cart:
        if row["product"] == product:
            row["quantity"] = float(row["quantity"]) + quantity
            return
    cart.append({"product": product, "price": price, "quantity": quantity})


# Removes an item from the shopping cart
def remove_item(product):
    global cart
    product = product.lower()
    index = 0
    for row in cart:
        if row["product"] == product:
            cart.pop(index)
            return
        index += 1
    print(f"Error! No {product} in the cart.")


# Updates the quantity of an item from the shopping cart
def update_quantity(product, quantity):
    global cart
    product = product.lower()
    for row in cart:
        if row["product"] == product:
            row["quantity"] = quantity
            return
    print(f"Sorry, no {product} currently added in the cart.")


# Displays the shopping cart
def view_cart():
    global cart
    if len(cart) != 0:
        print("{:<30} {:<15} {:<10} {:<15}".format("Product", "Price", "Quantity", "Subtotal"))
        total = 0
        for row in cart:
            subtotal = float(row["price"]) * float(row["quantity"])
            print("{:<30} {:<15} {:<10} {:<15}".format(row["product"].capitalize(), row["price"], row["quantity"], subtotal))
            total += subtotal
        print("{:<30} {:<15} {:<10} {:<15}".format("","","TOTAL", total))


if __name__ == "__main__":
    main()