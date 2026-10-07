customers = {
    "Alice": 750,
    "Bob": 2500,
    "Carol": 6000,
    "David": 1200
}

tiers = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

for customer, purchase in customers.items():
    if purchase < 1000:
        tier = "Bronze"
    elif purchase < 5000:
        tier = "Silver"
    else:
        tier = "Gold"

    tiers[tier] += 1

for tier, count in tiers.items():
    print(f"{tier}: {count} customers")