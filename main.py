current_package_weight = 0
shipped_packages = 0
item_number = 0
max_items = int(input("Please enter the maximum number of items to be shipped: "))
unused_capacity = 0
total_weight_sent = 0
total_unused_capacity = 0
package_with_most_unused_capacity = 0
most_unused_capacity = 0


while item_number < max_items:
    item_weight = float(input("Please enter the weight (kg) of the item. A single item should be 1-10kg: "))

    if item_weight == 0:
        break

    if not 1 <= item_weight <= 10:
        print("A single item should be 1-10kg. Please re-enter.")
        continue

    item_number = item_number + 1

    if current_package_weight + item_weight > 20:
        shipped_packages = shipped_packages + 1
        unused_capacity = 20 - current_package_weight
        current_package_weight = item_weight
        if unused_capacity > most_unused_capacity:
            package_with_most_unused_capacity = shipped_packages
            most_unused_capacity = unused_capacity

    else:
        current_package_weight = current_package_weight + item_weight
    total_weight_sent = total_weight_sent + item_weight

    print(f"Weight of current package is {current_package_weight} kg.")
    print(f"{shipped_packages} packages have been shipped.")

total_unused_capacity = shipped_packages * 20 - total_weight_sent
print(f"You have shipped {shipped_packages} packages")
print(f"Total weight of packages sent: {total_weight_sent} kg")
print(f"Total unused capacity: {total_unused_capacity} kg")

if package_with_most_unused_capacity > 0:
    print(f"Package number with most 'unused' capacity: {package_with_most_unused_capacity}")
    print(f"Amount of unused capacity in that package: {most_unused_capacity} kg")
else:
    print("No packages has unused capacity.")


