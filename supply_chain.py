warehouses = [
    {"name": "Jim's Distribution", "inventory": {"apples": 600, "bananas": 490}},
    {"name": "Bob's Produce Warehouse", "inventory": {"apples": 750, "bananas": 1000}},
    {"name": "Fruit Movers Inc", "inventory": {"apples": 730, "bananas": 550}}
]

totals = {}

for warehouse in warehouses:
    for product, quantity in warehouse["inventory"].items():
        if product in totals:
            totals[product] += quantity
        else:
            totals[product] = quantity

for product, total in totals.items():
    print(f"Total {product}: {total}")