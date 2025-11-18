# Define the menu of Rk.cafe
menu = dict(Pizza=50, Pasta=60, Burger=70, salad=70, coffee=80, SoftDrink=90, Juce=100)

print(menu)

#Greet
print("Welcome to Rk cafe")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order= ")
if item_1 in menu:
    order_total += menu[item_1]  #0 + 50
    print(f"Your item is {item_1} has been added to your order")
else:
    print(f"your item is {item_1} not available yet!")
    another_order = input("Do you want to order another item? (yes/no): ")
    if another_order == "yes":
        item_2 = input("Enter the name of Second item you want to order= ")
        if item_2 not in menu:
            print(f"Ordered item is {item_2} is not available!")
        else:
            order_total += menu[item_2]
            print(f"Your item is {item_2} has been added to your order")

    print(f"The total amount of items to pay is {order_total}")
