import re
from select import select
from typing import Any, Dict, List

from tabulate import tabulate

MAX_NAME_LEN: int = 20
PHONE_NUM_LEN: int = 10
PHONE_NUM_BEGIN: str = "09"

# Available foods list
# Why this structure for MAIN_MENU is good:
# 1. You can filter by category easily: foods["main_meal"].
# 2. Each item has structured details (name, price, quantity).
# 3. It is scalable: you can easily add fields like "delivery": True or "special_offer": False later.

MAIN_MENU: Dict[str, List[Dict[str, Any]]] = {
    "main_meal": [
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
    ],
}


###########
# HELPER FUNCTIONS
###########


def read_input(description: str) -> str:
    """Read a string input from the user and strip whitespace."""
    return input(description).strip()


def read_num(description: str) -> str:
    """Read numeric input (floats and integers) only."""
    while True:
        value = read_input(description)
        try:
            float(value)
        except ValueError as e:
            print(f"Please enter only numbers. {e}")
            continue
        return value


def read_range(description: str, start: int, end: int) -> int:
    """Accept a value and check that the number is within the predefined range."""
    while True:
        value = read_num(description)
        if value.isdigit():
            value_int = int(value)
            condition = value_int >= start and value_int <= end
            if condition:
                return value_int
            else:
                print(f"The choice should be between [{start}, {end}].")
                continue
        print("Something went wrong, try again.")
        continue


def find_id_in_main_menu(name: str, category: str) -> int:
    """Find and return the index of an item in the MAIN_MENU by its name."""
    for index, item in enumerate(MAIN_MENU[category]):
        if name == item["name"]:
            return index


########
# USER INFORMATION
#######


def get_customer_name(description: str) -> str:
    """Read and validate the customer's name."""
    while True:
        name = read_input(description)
        # Remove middle spaces to check if the remaining characters are alphabetic
        removed_mid_space = re.sub(r"\s+", "", name)
        if not removed_mid_space.isalpha():
            print("That is not a valid name.")
            continue

        if not (3 <= len(name) <= MAX_NAME_LEN):
            print(
                f"Your name length should be between 3 and {MAX_NAME_LEN} characters."
            )
            continue

        return name


def get_customer_phone(description: str) -> str:
    """Read and validate the customer's phone number."""
    while True:
        value = read_input(description)

        if len(value) != PHONE_NUM_LEN:
            print(f"The length should be exactly {PHONE_NUM_LEN} digits.")
            continue

        if value[:2] != PHONE_NUM_BEGIN:
            print(f"The number should start with {PHONE_NUM_BEGIN}.")
            continue
        if not value.isdigit():
            print("Enter only integer digits.")
            continue

        return value


##########################


# YOU CAN IMPROVE THE OUTPUT USING ZIM OR OTHER METHODS TO PRINT TABLES SIDE BY SIDE (mik, sami🔥🔥🔥)
def display_menu(menu: Dict[str, List[Dict[str, Any]]] = MAIN_MENU) -> None:
    """Display the food menu in a tabular format, grouped by category."""
    for cat_no, (category, items) in enumerate(menu.items(), start=1):
        print(f"\n-----------> Type {cat_no}. {category.upper()} <-----------")
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


###############
# FOOD ITEM SELECTION
###############


def select_food_category(
    description: str, menu: Dict[str, List[Dict[str, Any]]] = MAIN_MENU
) -> str:
    """Prompt the user to select a category after displaying the menu."""
    categories = list(menu.keys())
    if categories == []:
        print("Please add some products first in order to delete.")
        return ""
    total_category = len(categories)
    category_id = read_range(description, 1, total_category)
    category_id = category_id - 1  # normalize to 0-based index
    category = categories[category_id]

    return category  # return the name of the category


def select_food_item(
    description: str, category: str, menu: Dict[str, List[Dict[str, Any]]] = MAIN_MENU
) -> int:
    """Prompt the user to select an item within the chosen category."""
    total_item_in_selected_category = len(menu[category])
    item_id = read_range(description, 1, total_item_in_selected_category)

    return item_id - 1  # normalize to 0-based index


##########
# QUANTITY SELECTION
##########


def get_quantity(
    description: str,
    category: str,
    item_id: int,
    menu: Dict[str, List[Dict[str, Any]]] = MAIN_MENU,
) -> int:  # Dict[str, List[Dict[str, Any]]] BELEW DATATYPE YILHAL😁
    """Prompt the user to enter the quantity they want for a specific item."""
    cat = menu[category]
    selected_item = cat[item_id]
    stock_quantity = selected_item["stock_quantity"]
    while True:
        if stock_quantity >= 1:
            amount = read_range(description, 1, stock_quantity)
            selected_item["stock_quantity"] = stock_quantity - amount
            return amount

        print("There is no sufficient stock available. Please choose other item.")
        return 0


##############
# CART CRUD OPERATIONS
##############

cart: Dict[str, List[Dict[str, Any]]] = {}


# We might not need a class here; we could perform the same functionality with functions alone.
# However, the general aim of the project is for educational purposes.
# Therefore, I used a class here for both learning and logical organization of related items.
# The intention is to define methods that perform CRUD operations on the cart and the main menu.
class Cart:  #  NEED IMPROVEMENT
    def add(
        self,
        category: str,
        item_id: int,
        amount: int,
        menu: Dict[str, List[Dict[str, Any]]] = cart,
    ) -> None:
        """Add a selected item to the cart or update the quantity if it exists."""
        # add value if id does not exist
        if category not in menu:
            menu[category] = []

        selected_item = MAIN_MENU[category][item_id]
        for cart_item in menu[category]:
            if cart_item["name"] == selected_item["name"]:
                cart_item["stock_price"] += amount
                return

        new_item = selected_item.copy()
        new_item["stock_price"] = amount

        menu[category].append(new_item)

    def update(
        self,
        description: str,
        name: str,
        item_id: int,
        category: str,
        menu: Dict[str, List[Dict[str, Any]]] = cart,
    ) -> None:
        """Update the quantity of an item currently in the cart."""
        if category in cart:
            main_id = find_id_in_main_menu(
                name, category
            )  # Map the ID back to the main menu
            new_amount = get_quantity(description, category, item_id)
            menu[category][item_id]["stock_quantity"] = new_amount

    def delete(
        self,
        category_prompt: str,
        item_prompt: str,
        menu: Dict[str, List[Dict[str, Any]]] = cart,
    ) -> bool:
        """Delete a selected item from the menu."""
        category = select_food_category(category_prompt, menu=cart)
        item_id = select_food_item(item_prompt, category, menu=cart)
        if menu[category] == [] or menu[category][item_id] == []:
            print("Nothing to delete.")
            return False
        item = menu[category][item_id]
        menu[category].remove(item)
        return True

    def review_cart(self) -> None:  # needs modification
        """Display the current contents of the cart."""
        display_menu(menu=cart)

    def __str__(self) -> str:
        """String representation of the cart."""
        return f"cart: {cart}"


##########
# PAYMENT SYSTEM
##########


def get_price_each(
    category: str, item_id: int, menu: Dict[str, List[Dict[str, Any]]] = MAIN_MENU
) -> int:
    """Return the price of the selected item."""
    selected_item = menu[category][item_id]
    return selected_item["price"]


def calculate_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a given price and quantity."""
    return price * quantity


def calculate_total(menu: Dict[str, List[Dict[str, Any]]] = cart) -> float:
    """Calculate the total amount of the items in the cart."""
    total_price = 0.0

    for category, items in menu.items():
        for item in items:
            item_id = menu[category].index(item)
            amount = menu[category][item_id]["stock_quantity"]
            each_price = get_price_each(category, item_id, menu=menu)
            sub = calculate_subtotal(each_price, amount)
            total_price += sub
    return total_price


def process_payment(description: str, total_price: float) -> float:
    """Process payment, ensuring it meets the minimum 50% requirement."""
    _50per = total_price / 2
    attempt = 2
    while attempt > 0:
        paid = float(read_num(description))
        if paid >= _50per:
            return paid
        print(f"Your payment must be greater than or equal to {_50per}.")
        attempt -= 1
    return 0.0


##############
# CREATED ORDER VIEW
##############


def create_order(name: str, phone: str, total: float, status: str) -> None:  # untested
    """Display the user's name, phone number, total orders, and payment status."""
    print("\n🎉 Order created successfully 🎉")
    print(f"Name: {name}")
    print(f"Phone number: {phone}")
    print("--------------------")
    print("Orders:")

    for (
        category,
        values,
    ) in cart.items():
        item_category = category
        print(f" Type: {item_category}")
        for value in range(len(values)):  # Keeping logic compatible
            item_name = cart[category][value]["name"]
            item_price = cart[category][value]["price"]
            amount = cart[category][value]["stock_quantity"]
            print(f"  - {item_name}, Amount: {amount}, Price: {item_price}")

    print(f"Total price: {total}")
    print(f"Status: {status}")


def test_display() -> None:
    i = 0
    # while True:
    # User details entry removed for testing simplicity
    user_name = get_customer_name("Enter your name: ")
    user_phone = get_customer_phone("Enter your phone number: ")

    display_menu(MAIN_MENU)

    # Enter an item to the cart
    category = select_food_category("Please select category: ")
    item_id = select_food_item(f"Please select item from '{category}': ", category)

    item_name = MAIN_MENU[category][item_id]["name"]
    amount = get_quantity("How much do you want?: ", category, item_id)

    # Adding to cart
    cart_i = Cart()
    cart_i.add(category, item_id, amount)
    print(f"{amount} of {item_name} added to the cart from {category}.")

    print("_____________________________________________")
    total =calculate_total()
    pay = process_payment(f"It is time to pay total price: {total}$", total)
    status = "paid" if pay > 0 else "pending"
    
    create_order(user_name, user_phone, total, status)

    # # Updating cart
    # cart_i.review_cart()
    # print("Update your cart:")
    # print("Your cart is:")
    # cart_i.review_cart()

    # category = select_food_category(
    #     "Please select category from your cart: ", menu=cart
    # )
    # item_id = select_food_item(
    #     f"Which item do you want to update from '{category}'?: ",
    #     category,
    #     menu=cart,
    # )
    # name = cart[category][item_id]["name"]
    # cart_i.update("Enter amount: ", name, item_id, category)
    # print("Updated!")
    # cart_i.review_cart()

    # # if i % 2 != 0:
    #     is_deleted = cart_i.delete("Please enter category: ", "Please Enter item no: ")
    #     print("Done!") if is_deleted else print("Failed to delete!")
    #     cart_i.review_cart()
    # i += 1


test_display()
