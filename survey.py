preferences = ["coffee", "coffee", "coffee", "tea", "soda", "soda"]

counts = {}

for preference in preferences:
    if preference in counts:
        counts[preference] += 1
    else:
        counts[preference] = 1

total = len(preferences)

for product, count in counts.items():
    percentage = (count / total) * 100
    print(f"{product}: {percentage:.0f}%")