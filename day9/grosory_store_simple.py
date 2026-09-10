# Dictionary containing grocery items and their prices
prices = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 40
}

# Dictionary containing grocery items and quantities purchased
quantity = {
    "Rice": 2,
    "Sugar": 3,
    "Milk": 4,
    "Bread": 2
}

total_bill = 0

for item in prices:
    amount = prices[item] * quantity[item]
    total_bill += amount

print("Total Bill =", total_bill)