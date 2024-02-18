coins = [25, 10, 5]   # accepted denominations
amount_due = 50       # price of one bottle of Coke in cents
amount_paid = 0       # initially, user hasn't paid anything

# Prompt user to insert coins until the amount paid is at least the amount due
while amount_paid < amount_due:
    inserted_coin = int(input("Insert a coin (25, 10, or 5): "))
    if inserted_coin in coins:
        amount_paid += inserted_coin
        print("Amount due:", amount_due - amount_paid, "cents")
    else:
        print("Invalid coin. Please insert a valid coin.")

# Calculate the change owed to the user
change = amount_paid - amount_due

# Output the change owed to the user
if change > 0:
    print("Your change is:", change, "cents")
else:
    print("Thank you for your purchase!")
