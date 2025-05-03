# Write your code here

def print_earnings():
    items = {
        "Bubblegum": 202,
        "Toffee": 118,
        "Ice cream": 2250,
        "Milk chocolate": 1680,
        "Doughnut": 1075,
        "Pancake": 80
    }

    total_earnings = 0
    print("Earned amount:")
    for item, amount in items.items():
        print(f"{item}: ${amount}")
        total_earnings += amount

    print(f"\nIncome: ${total_earnings:.1f}")

# Call the function
print_earnings()

