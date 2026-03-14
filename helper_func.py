
from tabulate import tabulate

from typing import Any, Dict, List
MenuItem = Dict[str, Any]
MenuCategory = Dict[str, Any]
MenuType = List[MenuCategory]

def read_input(description: str) -> str:
    """Read a string input from the user and strip whitespace."""
    return input(description).strip()


def read_num(description: str) -> float:
    """Read numeric input (floats and integers) only."""
    while True:
        value = read_input(description)
        try:
            float(value)
        except ValueError as e:
            print(f"Please enter only numbers. {e}")
            continue
        return float(value)


def read_range(description: str, start: float, end: float) -> float:
    """Accept a value and check that the number is within the predefined range."""
    while True:
        value = read_num(description)

        condition = value >= start and value <= end
        if condition:
            return value
        else:
            print(f"The choice should be between [{start}, {end}].")
            continue


def display_menu(menu: MenuType ) -> None:
    """Display the food menu in a tabular format, grouped by category."""
    for cat_no, category_block in enumerate(menu, start=1):
        category = category_block["category"]
        items = category_block["items"]
        print(f"\ncategory {cat_no}. {category.upper()}")
        rows = []
        for item_no, item in enumerate(items, start=1):
            rows.append(
                [item_no, item["name"], f"{item['price']} Birr", item["stock_quantity"]]
            )
        print(
            tabulate(
                rows, headers=["No", "Name", "Price", "Quantity"], tablefmt="fancy_grid"
            )
        )

def display_food_category(menu:MenuType)->None:
    print("\nMenu Categories")
    for index, category in enumerate(menu, 1):
        print(f"{index}. {category['category'].upper()}")

def display_item_by_category(description, menu: MenuType)->None:
    display_food_category(menu)
    total_category = len(menu)
    category_id = int(read_range(description, 1, total_category))
    category_id = category_id - 1  # normalize to 0-based index
    display_category = [menu[category_id]]
    print("Selected category is: ")
    display_menu(display_category)

def select_food_category(description: str, menu: MenuType ) -> str:
    """Prompt the user to select a category ."""
    if menu == []:
        print("Please add some items into your cart first")
        return ""
    total_category = len(menu)
    category_id = int(read_range(description, 1, total_category))
    category_id = category_id - 1  # normalize to 0-based index
    category = menu[category_id]["category"]
    display_category = [menu[category_id]]
    print("Selected category is: ")
    display_menu(display_category)
    return category
