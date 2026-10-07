sales = {"Jessica": 3500, "Clarence": 9500, "Grace": 5000, "Derek": 12000, "Monica": 8000}

def calculate_commission(sales_amount):
    return sales_amount * 0.10

commissions = {}

for employee, amount in sales.items():
    commissions[employee] = calculate_commission(amount)

leaderboard = sorted(commissions.items(), key=lambda x: x[1], reverse=True)
# lambda function is used to sort the leaderboard by commission amount in descending order
print("Commission Leaderboard:")

for employee, commission in leaderboard:
    print(f"{employee}: ${commission:.2f}")