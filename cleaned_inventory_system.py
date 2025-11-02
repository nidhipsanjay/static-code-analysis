"""
Inventory Management System
Handles adding, removing, loading, saving, and reporting stock items.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item, qty=1, logs=None):
    """Add an item to stock with the given quantity."""
    if logs is None:
        logs = []
    if not isinstance(item, str):
        print("Invalid item name")
        return
    if not isinstance(qty, int) or qty < 0:
        print("Quantity must be a positive integer")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specific quantity of an item from stock."""
    if not isinstance(item, str):
        print("Invalid item name")
        return
    if not isinstance(qty, int) or qty <= 0:
        print("Invalid quantity")
        return

    if item in stock_data:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    else:
        print(f"Item '{item}' not found in stock data")


def get_qty(item):
    """Return the current quantity of an item (0 if missing)."""
    if not isinstance(item, str):
        print("Invalid item name")
        return 0
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        print(f"File not found: {file}")
    except json.JSONDecodeError:
        print(f"Error reading data from {file}")


def save_data(file="inventory.json"):
    """Save the current stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
    except OSError as e:
        print(f"Error saving data: {e}")


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given stock threshold."""
    if not isinstance(threshold, int) or threshold <= 0:
        print("Threshold must be a positive integer")
        return []
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function for testing inventory operations."""
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    add_item("orange", 1, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
