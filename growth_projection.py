revenue = float(input("Enter initial revenue: $"))
growth_rate = float(input("Enter annual growth rate (do not include %): "))

growth_rate = growth_rate / 100

print("Year | Projected Revenue")
print("-----------------------")

for year in range(1, 11):
    revenue = revenue * (1 + growth_rate)
    print(f"{year} | ${revenue:,.2f}")