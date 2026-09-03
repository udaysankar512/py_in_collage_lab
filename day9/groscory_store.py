# Q.1. creat a two dictinaries - one containing grocery items and their prices and another containing grocery items and quantity purchased by using the values from these two dictinaries compute the total bill

class ItemPrice:
    # method to calculate total bill
    def calculator(prices, quantities):
        total = 0
        print("\n--- Receipt ---")
        for item in quantities:
            if item in prices:
                cost = prices[item] * quantities[item]
                print(f"{item.capitalize()} ({quantities[item]} units) = Rs.{cost}")
                total += cost
        print(" - "*7)
        return total

    # method to let user pick items interactively
    def item_pick(prices):
        quantities = {}
        print("Items are abalable in the store :")
        for teams in prices:
             print(teams,end=" / ")
        print()
        while True:
            
            user = input("Enter item name (or 'done' to finish): ").lower()
            if user == "done":
                break
            if user in prices:
                qty = int(input(f"Enter quantity for {user}: "))
                quantities[user] = qty
            else:
                print("Item not found in grocery list.")
        return quantities


# - containing grocery items and their prices
grocery_items_price = {
    "rice": 60,
    "wheat": 45,
    "milk": 50,
    "eggs": 6,
    "sugar": 40,
    "oil": 120
}

# talck with the user / take input from the use 
quantities = ItemPrice.item_pick(grocery_items_price)
total_bill = ItemPrice.calculator(grocery_items_price, quantities)
print("Total Bill = Rs.", total_bill)