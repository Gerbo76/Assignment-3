prices = []

while True:
    price = float(input("Enter item price (0 to finish): $"))

    if price == 0:
        break

    prices.append(price)

total = sum(prices)

if len(prices) > 0:
    average = total / len(prices)
else:
    average = 0

print(f"Total purchase amount: ${total:.2f}")
print(f"Average item cost: ${average:.2f}")
print(f"Number of items bought: {len(prices)}")