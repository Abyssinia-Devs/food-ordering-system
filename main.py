import random
from user import user_flow
from owner import owner_flow
from typing import Any, Dict, List

MenuItem = Dict[str, Any]
MenuCategory = Dict[str, Any]
MenuType = List[MenuCategory]


def initialize_food_menu() -> MenuType:
    FOOD_MENU: MenuType = [
        {
            "category": "main_meal",
            "items": [
                {"name": "ፖስታ በቲማቲም ለብለብ", "price": 140, "stock_quantity": 10},
                {"name": "ፍርፍር", "price": 120, "stock_quantity": 8},
                {"name": "ሶያ", "price": 160, "stock_quantity": 10},
                {"name": "ሩዝ በአትክልት", "price": 150, "stock_quantity": 9},
                {"name": "ድንች ወጥ", "price": 110, "stock_quantity": 14},
                {"name": "መኮረኒ", "price": 135, "stock_quantity": 11},
                {"name": "በያይነት", "price": 170, "stock_quantity": 7},
                {"name": "ፍርፍር በፓስታ", "price": 145, "stock_quantity": 6},
                {"name": "ቲማቲም ለብለብ በፍርፍር", "price": 155, "stock_quantity": 13},
                {"name": "ስፔሻል ፍርፍር", "price": 180, "stock_quantity": 5},
                {"name": "እንቁላል ስልስ", "price": 125, "stock_quantity": 12},
                {"name": "እንቁላል ፍርፍር", "price": 135, "stock_quantity": 8},
            ],
        },
        {
            "category": "fast_food",
            "items": [
                {"name": "እርጥብ (normal)", "price": 95, "stock_quantity": 18},
                {"name": "እርጥብ (avocado)", "price": 110, "stock_quantity": 12},
                {"name": "እርጥብ (egg)", "price": 105, "stock_quantity": 15},
                {"name": "ኩኪስ, ስናክ, ብስኩት", "price": 70, "stock_quantity": 30},
                {"name": "እርጎ", "price": 80, "stock_quantity": 18},
            ],
        },
        {
            "category": "drinks",
            "items": [
                {"name": "የጀበና ቡና", "price": 60, "stock_quantity": 40},
                {"name": "macchiato", "price": 75, "stock_quantity": 35},
                {"name": "tea", "price": 65, "stock_quantity": 40},
                {"name": "ወተት", "price": 70, "stock_quantity": 33},
            ],
        },
        {
            "category": "breakfast",
            "items": [
                {"name": "እንጀራ በእንቁላል", "price": 120, "stock_quantity": 10},
                {"name": "ፉል", "price": 110, "stock_quantity": 12},
                {"name": "ቂጣ በማር", "price": 95, "stock_quantity": 15},
                {"name": "ቂጣ በእንቁላል", "price": 105, "stock_quantity": 10},
                {"name": "ገንፎ", "price": 100, "stock_quantity": 8},
            ],
        },
        {
            "category": "traditional_food",
            "items": [
                {"name": "ዶሮ ወጥ", "price": 220, "stock_quantity": 6},
                {"name": "ስጋ ወጥ", "price": 210, "stock_quantity": 7},
                {"name": "ክትፎ", "price": 250, "stock_quantity": 5},
                {"name": "ጎመን", "price": 120, "stock_quantity": 10},
                {"name": "ሽሮ ወጥ", "price": 140, "stock_quantity": 12},
            ],
        },
        {
            "category": "sandwiches",
            "items": [
                {"name": "egg sandwich", "price": 110, "stock_quantity": 15},
                {"name": "tuna sandwich", "price": 140, "stock_quantity": 10},
                {"name": "chicken sandwich", "price": 150, "stock_quantity": 9},
                {"name": "vegetable sandwich", "price": 120, "stock_quantity": 11},
            ],
        },
        {
            "category": "fresh_juice",
            "items": [
                {"name": "mango juice", "price": 110, "stock_quantity": 20},
                {"name": "avocado juice", "price": 120, "stock_quantity": 18},
                {"name": "papaya juice", "price": 105, "stock_quantity": 16},
                {"name": "mixed fruit juice", "price": 130, "stock_quantity": 14},
            ],
        },
        {
            "category": "desserts",
            "items": [
                {"name": "cake", "price": 90, "stock_quantity": 15},
                {"name": "ice cream", "price": 85, "stock_quantity": 20},
                {"name": "donut", "price": 70, "stock_quantity": 18},
                {"name": "fruit salad", "price": 95, "stock_quantity": 12},
            ],
        },
    ]
    return FOOD_MENU


def initialize_orders():
    orders = []
    return orders
orders = initialize_orders()
def main_menu():
    print(
        """
    ========================================
    ||       GS FOOD ORDERING PLATFORM     ||
    ========================================
"""
    )
    while True:
        print("\nWhat is your role:\n1.Customer\n2.Owner\n3.Exit")
        read_input = input(">")
        if not read_input.isdigit():
            print("\nPlease Enter only number.\n")
            continue
        choice = int(read_input)
        if choice > 3 or choice < 1:
            print("\nPlease enter only a number from 1 to 3\n")
            continue
        if choice == 1:
            user_flow( initialize_food_menu(), orders)
        if choice == 2:
            owner_flow(initialize_food_menu(), orders)
        if choice == 3:
            print("\nWe hope to serve you again soon!\n")
            return

if __name__ == "__main__":
    main_menu()
