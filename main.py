from inventory import Inventory


def print_header():
    print("\n" + "═" * 50)
    print("       📦  INVENTORY MANAGEMENT SYSTEM")
    print("═" * 50)


def print_menu():
    print("""
  1. View all products
  2. Add a product
  3. Delete a product
  4. Update quantity
  5. Update price
  6. Search by name
  7. Search by category
  8. View low stock (≤ 5 units)
  9. View total inventory value
  0. Exit
""")


def prompt_int(label: str) -> int:
    while True:
        try:
            return int(input(label).strip())
        except ValueError:
            print("  ✗ Please enter a whole number.")


def prompt_float(label: str) -> float:
    while True:
        try:
            return float(input(label).strip())
        except ValueError:
            print("  ✗ Please enter a number (e.g. 9.99).")


def display_products(products):
    if not products:
        print("  (no products found)")
    else:
        for p in products:
            print(" ", p)


def main():
    inv = Inventory()
    print_header()

    while True:
        print_menu()
        choice = input("  Select an option: ").strip()

        if choice == "1":
            print("\n── All Products ─────────────────────────────")
            display_products(inv.view_all())

        elif choice == "2":
            print("\n── Add Product ──────────────────────────────")
            pid      = input("  Product ID   : ").strip()
            name     = input("  Name         : ").strip()
            category = input("  Category     : ").strip() or "General"
            qty      = prompt_int("  Quantity     : ")
            price    = prompt_float("  Price ($)    : ")
            inv.add_product(pid, name, qty, price, category)

        elif choice == "3":
            print("\n── Delete Product ───────────────────────────")
            pid = input("  Product ID: ").strip()
            inv.delete_product(pid)

        elif choice == "4":
            print("\n── Update Quantity ──────────────────────────")
            pid = input("  Product ID  : ").strip()
            qty = prompt_int("  New quantity: ")
            inv.update_quantity(pid, qty)

        elif choice == "5":
            print("\n── Update Price ─────────────────────────────")
            pid   = input("  Product ID   : ").strip()
            price = prompt_float("  New price ($): ")
            inv.update_price(pid, price)

        elif choice == "6":
            print("\n── Search by Name ───────────────────────────")
            keyword = input("  Enter keyword: ").strip()
            display_products(inv.search_by_name(keyword))

        elif choice == "7":
            print("\n── Search by Category ───────────────────────")
            cat = input("  Enter category: ").strip()
            display_products(inv.search_by_category(cat))

        elif choice == "8":
            print("\n── Low Stock Alert (≤ 5 units) ──────────────")
            display_products(inv.low_stock())

        elif choice == "9":
            value = inv.total_value()
            print(f"\n  Total inventory value: ${value:,.2f}")

        elif choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        else:
            print("  ✗ Invalid option. Please choose 0–9.")


if __name__ == "__main__":
    main()
