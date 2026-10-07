revenue = [30, 90, 70, 20, 50, 60, 55]

for year, value in enumerate(revenue, start=1):
    bar_length = value // 10

    for i in range(1):
        bar = "#" * bar_length

    print(f"Year {year}: {bar}")