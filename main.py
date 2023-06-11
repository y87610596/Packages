current_package_weight = 0
shipped_packages = 0
item_number = 0


print("You can only send up to 10 items!!")

while True:
    item_weight = float(input("Please enter the weight (kg) of the item. A single item should be 1-10kg: "))

    if item_weight == 0:
        print(f"You have shipped {shipped_packages} packages")
        break

    if not 1 <= item_weight <= 10:
        print("A single item should be 1-10kg. Please re-enter.")
        continue

    item_number = item_number + 1
    if item_number == 11:
        print(f"You have shipped {shipped_packages} packages")
        break

    current_package_weight = current_package_weight + item_weight

    if current_package_weight > 20:
        shipped_packages = shipped_packages + 1
        current_package_weight = item_weight

    print(f"Weight of current package is {current_package_weight} kg.")
    print(f"{shipped_packages} packages have been shipped.")



