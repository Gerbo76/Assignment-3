portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0

for stock, data in portfolio.items():
    value = data["shares"] * data["price"]
    total_value += value

print(f"Total portfolio value: ${total_value:,.2f}")