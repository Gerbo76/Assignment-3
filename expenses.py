expenses = {
    "Travel": [500, 600, 55, 47],
    "Meals": [55, 47, 100, 19, 30],
    "Supplies": [20, 15, 30, 25]
}

grand_total = 0

for category, amounts in expenses.items():
    category_total = 0

    for amount in amounts:
        category_total += amount

    print(f"{category}: ${category_total:.2f}")

    grand_total += category_total

print(f"Grand Total: ${grand_total:.2f}")