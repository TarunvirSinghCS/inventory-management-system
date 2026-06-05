import json
import os
from product import Product


class Inventory:
    """Manages the collection of products with full CRUD and file persistence."""

    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.products: dict[str, Product] = {}
        self.load_from_file()

    # ── CRUD ──────────────────────────────────────────────────────────────────

    def add_product(self, product_id: str, name: str, quantity: int, price: float, category: str = "General") -> bool:
        """Add a new product. Returns False if the ID already exists."""
        if product_id in self.products:
            print(f"  ✗ Product ID '{product_id}' already exists.")
            return False
        self.products[product_id] = Product(product_id, name, quantity, price, category)
        self.save_to_file()
        print(f"  ✓ Product '{name}' added successfully.")
        return True

    def delete_product(self, product_id: str) -> bool:
        """Delete a product by ID. Returns False if not found."""
        if product_id not in self.products:
            print(f"  ✗ Product ID '{product_id}' not found.")
            return False
        name = self.products[product_id].name
        del self.products[product_id]
        self.save_to_file()
        print(f"  ✓ Product '{name}' deleted successfully.")
        return True

    def update_quantity(self, product_id: str, new_quantity: int) -> bool:
        """Update the quantity of an existing product."""
        if product_id not in self.products:
            print(f"  ✗ Product ID '{product_id}' not found.")
            return False
        if new_quantity < 0:
            print("  ✗ Quantity cannot be negative.")
            return False
        self.products[product_id].quantity = new_quantity
        self.save_to_file()
        print(f"  ✓ Quantity updated to {new_quantity}.")
        return True

    def update_price(self, product_id: str, new_price: float) -> bool:
        """Update the price of an existing product."""
        if product_id not in self.products:
            print(f"  ✗ Product ID '{product_id}' not found.")
            return False
        if new_price < 0:
            print("  ✗ Price cannot be negative.")
            return False
        self.products[product_id].price = new_price
        self.save_to_file()
        print(f"  ✓ Price updated to ${new_price:.2f}.")
        return True

    # ── SEARCH / VIEW ─────────────────────────────────────────────────────────

    def search_by_name(self, keyword: str) -> list[Product]:
        """Return all products whose name contains the keyword (case-insensitive)."""
        keyword = keyword.lower()
        return [p for p in self.products.values() if keyword in p.name.lower()]

    def search_by_category(self, category: str) -> list[Product]:
        """Return all products in a given category (case-insensitive)."""
        category = category.lower()
        return [p for p in self.products.values() if p.category.lower() == category]

    def get_product(self, product_id: str) -> Product | None:
        """Return a single product by ID, or None."""
        return self.products.get(product_id)

    def view_all(self) -> list[Product]:
        """Return all products sorted by name."""
        return sorted(self.products.values(), key=lambda p: p.name.lower())

    def low_stock(self, threshold: int = 5) -> list[Product]:
        """Return products with quantity at or below the threshold."""
        return [p for p in self.products.values() if p.quantity <= threshold]

    def total_value(self) -> float:
        """Return total inventory value (sum of price × quantity)."""
        return sum(p.price * p.quantity for p in self.products.values())

    # ── PERSISTENCE ───────────────────────────────────────────────────────────

    def save_to_file(self) -> None:
        """Serialize the inventory to JSON."""
        data = [p.to_dict() for p in self.products.values()]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self) -> None:
        """Load inventory from JSON (silently skips if file doesn't exist yet)."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
            for item in data:
                p = Product.from_dict(item)
                self.products[p.product_id] = p
        except (json.JSONDecodeError, KeyError) as e:
            print(f"  ⚠ Warning: could not load data file ({e}). Starting fresh.")
