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

    print(f"\nIncome: ${total_earnings}")

    print("Staff expenses:", end=" ")
    staff_expenses = int(input())
    print("Other expenses:", end=" ")
    other_expenses = int(input())

    net_income = total_earnings - staff_expenses - other_expenses
    print(f"Net income: ${net_income}")


# Call the function
print_earnings()

