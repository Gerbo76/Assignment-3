loan = float(input("Enter loan amount: $"))
interest_rate = float(input("Enter annual interest rate (do not include %): "))
payment = float(input("Enter monthly payment: $"))

balance = loan
monthly_rate = (interest_rate / 100) / 12
months = 0

while balance > 0:
    interest = balance * monthly_rate
    balance += interest
    balance -= payment
    months += 1

print(f"It takes {months} months to pay off the loan.")