# Cleaned inventory_system.py
import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_item(item=None, qty=0, logs=None):
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid item or quantity type provided.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    try:
        if item in stock_data and stock_data[item] >= qty:
            stock_data[item] -= qty
        else:
            logging.warning(f"Cannot remove {qty} from {item} (insufficient stock or item missing)")
    except Exception as e:
        logging.error(f"Error removing item: {e}")


def get_qty(item):
    return stock_data.get(item, 0)


def check_low_items(threshold=5):
    return [item for item, qty in stock_data.items() if qty < threshold]


def save_data(filename='stock.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(stock_data, f)
    except IOError as e:
        logging.error(f"Error saving data: {e}")


def load_data(filename='stock.json'):
    global stock_data
    try:
        with open(filename, 'r') as f:
            stock_data = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Error loading data: {e}")


def print_data():
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def main():
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()

