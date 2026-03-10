MAX_NAME_LEN = 20
PHONE_NUM_LEN = 10
PHONE_NUM_BEGIN = "09"

# Available foods list
"""Why this structure for food_menu is good:
You can filter by category easily: foods["main_meal"].

Each item has structured details (name, price, quantity).

It is scalable: you can later add fields like "delivery": True or "special_offer": False.
"""
food_menu = {
    "main_meal": [
        {"name": "ፖስታ በቲማቲም ለብለብ", "price": 140, "stock_quantity": 12},
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
    "fast_food": [
        {"name": "እርጥብ (normal)", "price": 95, "stock_quantity": 18},
        {"name": "እርጥብ (avocado)", "price": 110, "stock_quantity": 12},
        {"name": "እርጥብ (egg)", "price": 105, "stock_quantity": 15},
        {"name": "ኩኪስ, ስናክ, ብስኩት", "price": 70, "stock_quantity": 30},
        {"name": "እርጎ", "price": 80, "stock_quantity": 18},
    ],
    "drinks": [
        {"name": "የጀበና ቡና", "price": 60, "stock_quantity": 40},
        {"name": "macchiato", "price": 75, "stock_quantity": 35},
        {"name": "tea", "price": 65, "stock_quantity": 40},
        {"name": "ወተት", "price": 70, "stock_quantity": 33},
    ]
}



def read_input(description: str) -> str:
    return input(description).strip()

def is_int(value: any) -> bool:
    return True if value.isdigit() else False
    
def read_range(description, start, end):
    """Accept a value and check that the number is within the predefined range."""
    while True:
        value = read_input(description)
        if not is_int:
            print("Please enter only a number.")
        value = int(value)
        if value >= start and value <= end:
            return value
        print(f"The choice should be between [{start}, {end}]")
        
    
def get_customer_name(description: str) -> str:
    """Read and validate a customer's name."""
    while True:
        name = read_input(description)

        if not name.isalpha():
            print("That is not a correct name.")
            continue

        if len(name) > MAX_NAME_LEN:
            print(f"Your name length should be less than or equal to {MAX_NAME_LEN}.")
            continue

        return name


def get_customer_phone(description: str) -> str:
    """Read and validate a customer's phone number."""
    while True:
        value = read_input(description)

        if len(value) != PHONE_NUM_LEN:
            print(f"The length should be exactly {PHONE_NUM_LEN}.")
            continue

        if value[:2] != PHONE_NUM_BEGIN:
            print(f"The number should start with {PHONE_NUM_BEGIN}.")
            continue

        if not is_int(value):
            print("Please enter only numbers.")
            continue

        return value
    

def select_food_item(food_menu):
    """After displaying the menu, the user selects a category and then an item within that category."""
    categories = list(food_menu.keys())
    total_category = len(categories)
    
    category_id = read_range("Which category do you want ", 1, total_category)
    
    selected_category = categories[category_id-1]
    # You can add a function (or any approach you prefer) to print only items in the selected category,
    # so the user can clearly choose from selected_category.
    # In this case, we assume the user can refer back to the main displayed menu
    # and select a specific item from there.
    total_item_in_selected_category = len(food_menu[selected_category])
    item_id = read_range("Select an item",  1, total_item_in_selected_category)
    
    return category_id, item_id


    
# First, run select_food_item, then use category_id and item_id.
def get_stock_quantity(food_menu, category_id, item_id):
    """Return the selected amount and decrease stock_quantity after selection."""
    categories = list(food_menu.keys())
    category = food_menu[categories[category_id]]
    selected_item = category[item_id]
    stock_quantity = selected_item['stock_quantity']
    amount = read_range("Enter amount: ", 1, stock_quantity)
    
    # Decrease the stock quantity.
    stock_quantity = stock_quantity-amount
    return amount