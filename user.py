import re
from typing import Any, Dict, List, Optional
import random
from tabulate import tabulate

MAX_NAME_LEN: int = 20
PHONE_NUM_LEN: int = 10
PHONE_NUM_BEGIN: str = "09"

MenuItem = Dict[str, Any]
MenuCategory = Dict[str, Any]
MenuType = List[MenuCategory]

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


def find_id_in_FOOD_MENU (name: str, category: str, FOOD_MENU: MenuType) -> int:
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

def generate_next_order_id(orders):
    while True:
        rand_int = random.randint(1, 1000)
        next_order_id = "ORD-" + f"{str(rand_int):0>3}"
        if next_order_id in orders:
            continue
        return next_order_id
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
###############
# FOOD ITEM SELECTION
###############


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


def select_food_item(
    description: str, category: str, menu: MenuType
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
    menu: MenuType,
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

    def add_to_cart(self,FOOD_MENU) -> None:
        """add_to_cart a selected item to the CART or update the quantity if it exists."""
        display_food_category(FOOD_MENU)
        category = select_food_category("Please select category: ", menu=FOOD_MENU )
        if category == "":
            return
        item_id = select_food_item(f"Please select item from '{category}': ", category, menu=FOOD_MENU)
        if item_id == -1:
            return
        amount = get_quantity("How much do you want? : ", category, item_id, FOOD_MENU )
        if amount == 0:
            return
        sub_total = calculate_subtotal(get_price_each(category, item_id,FOOD_MENU), amount)

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

    def update(self, FOOD_MENU) -> None:
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
            name, category,FOOD_MENU
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

    def delete(self,FOOD_MENU) -> None:
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
        main_id = find_id_in_FOOD_MENU (item["name"], category, FOOD_MENU)
        if main_id != -1:
            get_items_by_category(FOOD_MENU , category)[main_id]["stock_quantity"] += (
                item["stock_quantity"]
            ) # put stock quantity back to food_menu

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


def get_price_each(category: str, item_id: int, menu: MenuType ) -> int:
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




def create_order(cart, name, phone, order):  # untested
    if cart == []:
        print("Please first add some items in your cart to create an order")
        return
    items = []
    for category in cart:
        for item in category["items"]:
            items.append(item)
    total_price = calculate_total(menu=cart)
    pay = process_payment(
        f"It is time to pay. Please pay at least {total_price / 2.0} Birr: $",
        total_price,
    )
    orderId =generate_next_order_id(order)
    status = (
        "paid" if pay == total_price else "pending"
    )  # WHEN THE USER DOES NOT FULLY PAID I USED PENDING....
    order_record = {
        "order_id":orderId,
        "name": name,
        "phone": phone,
        "items":items,
        "status": status,
        "total_price": total_price,
    }
    order.append(order_record)
    print("\n🎉 Order created successfully 🎉")

    return order_record


def print_receipt(order_record, menu):
    """Display the user's name, phone number, total orders, payment status and clear the cart"""
    if order_record is None:
        return
    else:
        order_id = order_record["order_id"]
        name = order_record["name"]
        phone = order_record["phone"]
        status = order_record["status"]
        total_price = order_record["total_price"]
    print(f"order id: {order_id}")
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


def user_flow(menu=[] , order=None):
    if not menu:
        print("All Items are selled!, Thanks.")
        return
    name = get_customer_name("Enter your name: ")
    phone = get_customer_phone("Enter your phone number: ")
    print("""
    ========================================
    ||       GS FOOD ORDERING PLATFORM       ||
    ========================================
""")
    print(f"Welcome, {name.capitalize()}")
    cart = Cart()
    while True:
        print("\n1. Display full menu")
        print("2. view food by catagory")
        print("3. Add to cart")
        print("4. Update cart")
        print("5. Display cart")
        print("6. Delete item")
        print("7. Create order")
        print("0. Exit")

        choice = read_range("> ", 0, 7)

        match choice:
            case 1:
                display_menu(menu)
            case 2:
                display_item_by_category("Please select category:",menu)
            case 3:
                cart.add_to_cart(menu)
            case 4:
                cart.update(menu)
            case 5:
                cart.review_cart()
            case 6:
                cart.delete(menu)
            case 7:
                order_record = create_order(cart.cart, name, phone, order)
                print_receipt(order_record, menu=cart.cart)
                print(order)
            case 0:
                print("Thank you for visiting. Have a great day!")
                break

    return
