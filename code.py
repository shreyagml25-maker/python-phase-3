# Inventory Stock Analysis System - Phase 3

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
stock = [10, 25, 15, 12, 8]
minimum = [5, 10, 5, 5, 5]
price = [50000, 500, 1200, 8000, 1500]

while True:
    print("\n--- INVENTORY STOCK ANALYSIS ---")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Low Stock Alert")
    print("5. Stock Summary")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print(f"\n{'Product':<16} {'Stock':<10} {'Price (Rs.)':<12}")
        print("-" * 40)
        for i in range(len(products)):
            print(f"{products[i]:<16} {stock[i]:<10} {price[i]:<12.2f}")

    elif choice == "2":
        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty.")
        elif name.lower() in [p.lower() for p in products]:
            print("Product already exists!")
        else:
            try:
                qty = int(input("Enter quantity: "))
                cost = float(input("Enter price: "))
                min_qty = int(input("Enter minimum stock: "))

                if qty < 0 or cost < 0 or min_qty < 0:
                    print("Values cannot be negative!")
                else:
                    products.append(name)
                    stock.append(qty)
                    price.append(cost)
                    minimum.append(min_qty)
                    print("Product added successfully!")
            except ValueError:
                print("Invalid input! Quantity and minimum stock must be integers, and price must be a valid number.")

    elif choice == "3":
        name = input("Enter product name: ").strip()
        found = False

        for i in range(len(products)):
            if products[i].lower() == name.lower():
                try:
                    qty = int(input(f"Enter new stock quantity for '{products[i]}': "))
                    if qty >= 0:
                        stock[i] = qty
                        print("Stock updated successfully!")
                    else:
                        print("Quantity cannot be negative.")
                except ValueError:
                    print("Please enter a valid whole number for quantity.")
                found = True
                break

        if not found:
            print("Product not found!")

    elif choice == "4":
        print("\n--- LOW STOCK PRODUCTS ---")
        found = False

        print(f"{'Product':<16} {'Current Stock':<15} {'Minimum Required':<18}")
        print("-" * 50)
        for i in range(len(products)):
            if stock[i] <= minimum[i]:
                print(f"{products[i]:<16} {stock[i]:<15} {minimum[i]:<18}")
                found = True

        if not found:
            print("All products are above minimum required stock levels.")

    elif choice == "5":
        total_products = len(products)
        total_stock = sum(stock)
        total_value = sum(stock[i] * price[i] for i in range(len(products)))

        print("\n--- STOCK SUMMARY ---")
        print(f"Total Products:         {total_products}")
        print(f"Total Stock Units:      {total_stock}")
        print(f"Total Inventory Value:  Rs. {total_value:,.2f}")

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 6.")
