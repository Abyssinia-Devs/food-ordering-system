import re
from typing import Any, Dict, List, Optional

from tabulate import tabulate

MAX_NAME_LEN: int = 20
PHONE_NUM_LEN: int = 10
PHONE_NUM_BEGIN: str = "09"

MenuItem = Dict[str, Any]
MenuCategory = Dict[str, Any]
MenuType = List[MenuCategory]

FOOD_MENU : MenuType = [
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
]


###########
# HELPER FUNCTIONS
###########


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


def get_category_block(menu: MenuType, category: str) -> Optional[MenuCategory]:
    """return category bloc or none"""
    for category_block in menu:
        if category_block["category"] == category:
            return category_block
    return None


def get_items_by_category(menu: MenuType, category: str) -> List[MenuItem]:
    """return items from the given category"""
    category_block = get_category_block(menu, category)
    if category_block is None:
        return []
    return category_block["items"]


def find_id_in_FOOD_MENU (name: str, category: str) -> int:
    """Find and return the index of an item in the FOOD_MENU  by its name."""
    for index, item in enumerate(get_items_by_category(FOOD_MENU , category)):
        if name == item["name"]:
            return index
    return -1


def get_or_create_category(menu: MenuType, category: str) -> MenuCategory:
    """Helper function cart to match current menu structure"""
    category_block = get_category_block(menu, category)
    if category_block is None:
        category_block = {"category": category, "items": []}
        menu.append(category_block)
    return category_block


########
# USER INFORMATION
#######


def get_customer_name(description: str) -> str:
    """Read and validate the customer's name."""
    while True:
        name = read_input(description)
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


def display_menu(menu: MenuType = FOOD_MENU ) -> None:
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


###############
# FOOD ITEM SELECTION
###############


def select_food_category(description: str, menu: MenuType = FOOD_MENU ) -> str:
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


def select_food_item(
    description: str, category: str, menu: MenuType = FOOD_MENU 
) -> int:
    """Prompt the user to select an item within the chosen category."""
    total_item_in_selected_category = len(get_items_by_category(menu, category))
    if total_item_in_selected_category == 0:
        print("Item not found!")
        return -1
    item_id = int(read_range(description, 1, total_item_in_selected_category))

    return item_id - 1


##########
# QUANTITY SELECTION
##########


def get_quantity(
    description: str,
    category: str,
    item_id: int,
    menu: MenuType = FOOD_MENU ,
) -> int:
    """Prompt the user to enter the quantity they want for a specific item."""
    cat = get_items_by_category(menu, category)
    selected_item = cat[item_id]
    stock_quantity = selected_item["stock_quantity"]
    while True:
        if stock_quantity >= 1:
            amount = int(read_range(description, 1, stock_quantity))
            selected_item["stock_quantity"] = stock_quantity - amount
            return amount

        print("There is no sufficient stock available. Please choose other item.")
        return 0


##############
# CART CRUD OPERATIONS
##############


class Cart:
    def __init__(self):
        self.cart: MenuType = []

    def add_to_cart(
        self,
    ) -> None:
        """add_to_cart a selected item to the CART or update the quantity if it exists."""
        display_menu()
        category = select_food_category("Please select category: ", menu=FOOD_MENU )
        if category == "":
            return
        item_id = select_food_item(
            f"Please select item from '{category}': ", category, menu=FOOD_MENU 
        )
        if item_id == -1:
            return
        amount = get_quantity("How much do you want? : ", category, item_id, FOOD_MENU )
        if amount == 0:
            return
        sub_total = calculate_subtotal(get_price_each(category, item_id), amount)

        cart_category = get_or_create_category(self.cart, category)

        selected_item = get_items_by_category(FOOD_MENU , category)[item_id]
        for cart_item in cart_category["items"]:
            if cart_item["name"] == selected_item["name"]:
                cart_item["stock_quantity"] += amount
                cart_item["sub_price"] += sub_total
                print("Item added to CART successfully 🎉.")
                return

        new_item = selected_item.copy()
        new_item["sub_price"] = sub_total
        new_item["stock_quantity"] = amount
        cart_category["items"].append(new_item)
        print("Item added to CART successfully 🎉.")

    def update(
        self,
    ) -> None:
        """Update the quantity of an item currently in the CART."""
        category = select_food_category("Please select category: ", menu=self.cart)
        if category == "":
            return
        item_id = select_food_item(
            f"Which item do you want to update from '{category}'?: ",
            category,
            menu=self.cart,
        )
        if item_id == -1:
            return

        cart_items = get_items_by_category(self.cart, category)
        name = cart_items[item_id]["name"]
        main_id = find_id_in_FOOD_MENU (
            name, category
        )  # Map the ID back to the main menu
        previus_amount = cart_items[item_id]["stock_quantity"]
        get_items_by_category(FOOD_MENU , category)[main_id]["stock_quantity"] += (
            previus_amount  # Put it back
        )
        new_amount = get_quantity(
            f"Enter new Quantity for {name}: ", category, main_id, FOOD_MENU 
        )
        cart_items[item_id]["stock_quantity"] = new_amount
        each_price = cart_items[item_id]["price"]
        cart_items[item_id]["sub_price"] = calculate_subtotal(each_price, new_amount)
        print("Updated 🎉")

    def delete(self) -> None:
        """Delete a selected item from the CART menu."""
        category = select_food_category(f"Please select category: ", menu=self.cart)
        if category == "":
            print("Failed to delete!")
            return
        item_id = select_food_item(
            f"Which item do you want to delete from '{category}'?: ",
            category,
            menu=self.cart,
        )
        if item_id == -1:
            print("Faild to delete!")
            return

        # CHANGED: delete now works with category objects and restores stock to FOOD_MENU .
        cart_category = get_category_block(self.cart, category)
        if cart_category is None:
            print("Faild to delete!")
            return

        item = cart_category["items"][item_id]
        main_id = find_id_in_FOOD_MENU (item["name"], category)
        if main_id != -1:
            get_items_by_category(FOOD_MENU , category)[main_id]["stock_quantity"] += (
                item["stock_quantity"]
            )

        cart_category["items"].remove(item)
        if cart_category["items"] == []:
            self.cart.remove(cart_category)
        print("Item deleted successfully 🎉")
        return

    def review_cart(self) -> None:
        """Display the current contents of the CART."""
        if self.cart == []:
            print("Please first add some items in your cart to review your cart.")
            return

        for cat_no, category_block in enumerate(self.cart, start=1):
            category = category_block["category"]
            items = category_block["items"]
            print(f"\n Category {cat_no}. {category.upper()}")
            rows = []
            for item_no, item in enumerate(items, start=1):
                rows.append(
                    [
                        item_no,
                        item["name"],
                        f"{item['price']} Birr",
                        item["stock_quantity"],
                        f"{item['sub_price']} Birr",
                    ]
                )
            print(
                tabulate(
                    rows,
                    headers=["No", "Name", "Price", "Quantity", "Sub Price"],
                    tablefmt="fancy_grid",
                )
            )
        total_price = calculate_total(self.cart)
        print(f"\n Total price: {total_price} Birr")

    def __str__(self) -> str:
        return f"CART: {self.cart}"


##########
# PAYMENT SYSTEM
##########


def get_price_each(category: str, item_id: int, menu: MenuType = FOOD_MENU ) -> int:
    """Return the price of the selected item."""
    selected_item = get_items_by_category(menu, category)[item_id]
    return selected_item["price"]


def calculate_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a given price and quantity."""
    return price * quantity


def calculate_total(menu: MenuType) -> float:
    """Calculate the total amount of the items in the CART."""
    total_price = 0.0

    for category_block in menu:
        for item in category_block["items"]:
            sub = item["sub_price"]
            total_price += sub
    return total_price


def process_payment(description: str, total_price: float) -> float:
    _50per = total_price / 2
    paid = read_range(description, _50per, total_price)
    return paid


##############
# CREATED ORDER VIEW
##############

order_record = {}


def create_order(cart, name, phone):  # untested
    if cart == []:
        print("Please first add some items in your cart to create an order")
        return

    total_price = calculate_total(menu=cart)
    pay = process_payment(
        f"It is time to pay. Please pay at least {total_price / 2.0} Birr: $",
        total_price,
    )
    status = (
        "paid" if pay == total_price else "pending"
    )  # WHEN THE USER DOES NOT FULLY PAID I USED PENDING....

    order_record = {
        "name": name,
        "phone": phone,
        "status": status,
        "total_price": total_price,
    }
    print("\n🎉 Order created successfully 🎉")

    return order_record


def print_receipt(order_record, menu):
    """Display the user's name, phone number, total orders, payment status and clear the cart"""
    if order_record is None:
        return
    else:
        name = order_record["name"]
        phone = order_record["phone"]
        status = order_record["status"]
        total_price = order_record["total_price"]
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Status: {status}")
    print(f"Total Price: {total_price}")
    print("Ordered Items \n")
    rows = []
    for category_block in menu:
        for value in category_block["items"]:
            rows.append([value["stock_quantity"], value["name"]])
    print(tabulate(rows, headers=["Quantity", "Item"]))

    menu.clear()  # clear cart


def user_flow(menu=FOOD_MENU , order=None):
    name = get_customer_name("Enter your name: ")
    phone = get_customer_phone("Enter your phone number: ")
    print("Welcome 🎉")
    display_menu()
    cart = Cart()
    while True:
        print("\n1. Display menu again")
        print("2. Add to cart")
        print("3. Update cart")
        print("4. Display cart")
        print("5. Delete item")
        print("6. Create order")
        print("0. Exit")

        choice = read_range("> ", 0, 6)

        match choice:
            case 1:
                display_menu(menu=FOOD_MENU )
            case 2:
                cart.add_to_cart()
            case 3:
                cart.update()
            case 4:
                cart.review_cart()
            case 5:
                cart.delete()
            case 6:
                order_record = create_order(cart.cart, name, phone)
                print_receipt(order_record, menu=cart.cart)
            case 0:
                break

    return


user_flow()