# List to store item dictionaries
items = []

num = int(input("Enter the number of items: "))

# Collect item data
for i in range(num):
    name = input(f"\nEnter name of item {i+1}: ")
    quantity = int(input(f"Enter quantity of '{name}': "))
    price = float(input(f"Enter price of one unit of '{name}': "))

    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "subtotal": quantity * price
    }
    items.append(item)

# Function to display bill
def display_bill(items):
    print("\n" + "="*45)
    print("{:<20} {:>6} {:>10} {:>10}".format("Item", "Qty", "Price", "Total"))
    print("-"*45)

    total = 0
    for item in items:
        print("{:<20} {:>6} {:>10.2f} {:>10.2f}".format(
            item["name"], item["quantity"], item["price"], item["subtotal"]
        ))
        total += item["subtotal"]

    print("-"*45)
    print(f"{'TOTAL':<20} {'':>6} {'':>10} ₹{total:>9.2f}")

    if total > 500:
        discount = total * 0.10
        final_price = total - discount
        print(f"{'DISCOUNT (10%)':<36} -₹{discount:>8.2f}")
        print(f"{'FINAL PRICE':<36} ₹{final_price:>8.2f}")
    else:
        print("No discount applied.")

    print("="*45)

# Show the final bill
display_bill(items)
