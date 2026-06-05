# 📦 Inventory Management System

A command-line inventory management application built with Python. Supports full CRUD operations, persistent JSON storage, low-stock alerts, and inventory value reporting.

---

## Features

| Feature | Description |
|---|---|
| **Add product** | Create a product with ID, name, category, quantity, and price |
| **Delete product** | Remove a product by ID |
| **Update quantity** | Change stock level for any product |
| **Update price** | Change the price for any product |
| **Search by name** | Find products using a keyword |
| **Search by category** | Filter products by category |
| **Low stock alert** | List all products with ≤ 5 units remaining |
| **Total value** | Calculate total inventory value (price × quantity) |
| **Persistent storage** | All data saved automatically to `data.json` |

---

## Project Structure

```
inventory-management-system/
│
├── main.py          # CLI entry point and menu logic
├── inventory.py     # Inventory class — manages all products
├── product.py       # Product class — data model
├── data.json        # Auto-generated persistent storage
├── requirements.txt # No third-party dependencies required
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10 or higher

### Run the app

```bash
git clone https://github.com/YOUR_USERNAME/inventory-management-system.git
cd inventory-management-system
python main.py
```

No `pip install` needed — this project uses only the Python standard library.

---

## Usage

```
══════════════════════════════════════════════════
       📦  INVENTORY MANAGEMENT SYSTEM
══════════════════════════════════════════════════

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
```

### Example: Adding a product
```
Select an option: 2

── Add Product ──────────────────────────────
  Product ID   : P010
  Name         : Mechanical Keyboard
  Category     : Electronics
  Quantity     : 15
  Price ($)    : 89.99
  ✓ Product 'Mechanical Keyboard' added successfully.
```

---

## Concepts Demonstrated

- **Object-Oriented Programming** — `Product` and `Inventory` classes
- **File I/O** — Reading and writing JSON with the `json` module
- **Error handling** — Input validation and graceful error messages
- **Data structures** — Dictionary-based in-memory storage
- **CLI design** — Clean, navigable menu interface

---

## Future Improvements

- [ ] Export inventory to CSV
- [ ] Add a web frontend (Flask)
- [ ] User authentication
- [ ] Transaction history / audit log

---

## License

MIT
