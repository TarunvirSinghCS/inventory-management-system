class Product:
    """Represents a single product in the inventory."""

    def __init__(self, product_id: str, name: str, quantity: int, price: float, category: str = "General"):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def to_dict(self) -> dict:
        """Convert product to dictionary for JSON storage."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        """Create a Product from a dictionary (loaded from JSON)."""
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            quantity=data["quantity"],
            price=data["price"],
            category=data.get("category", "General")
        )

    def __str__(self) -> str:
        return (
            f"[{self.product_id}] {self.name} | "
            f"Category: {self.category} | "
            f"Qty: {self.quantity} | "
            f"Price: ${self.price:.2f}"
        )
