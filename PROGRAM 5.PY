# Online Shopping Product Price Sorter

# Sample product list (name + price)
products = [
    {"name": "Shoes", "price": 1299},
    {"name": "T-Shirt", "price": 499},
    {"name": "Watch", "price": 1999},
    {"name": "Jeans", "price": 899},
    {"name": "Bag", "price": 750}
]

print("Choose sorting option:")
print("1. Price Low → High")
print("2. Price High → Low")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        sorted_products = sorted(products, key=lambda x: x["price"])
        print("\nProducts sorted Low → High:")
        for p in sorted_products:
            print(f"{p['name']} - ₹{p['price']}")

    case 2:
        sorted_products = sorted(products, key=lambda x: x["price"], reverse=True)
        print("\nProducts sorted High → Low:")
        for p in sorted_products:
            print(f"{p['name']} - ₹{p['price']}")

    case _:
        print("Invalid choice!")
