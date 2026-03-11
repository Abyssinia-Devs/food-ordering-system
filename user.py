from tabulate import tabulate

MAX_NAME_LEN = 20
PHONE_NUM_LEN = 10
PHONE_NUM_BEGIN = "09"

# Available foods list
# Why this structure for food_menu is good:
# You can filter by category easily: foods["main_meal"].
# Each item has structured details (name, price, quantity).
# It is scalable: you can later add fields like "delivery": True or "special_offer": False.

food_menu = {
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
ALL_CATEGORIES = list(food_menu.keys())


def read_input(description: str) -> str:
    return input(description).strip()


def read_int(description) -> int:
    while True:
        value = read_input(description)
        if not value.isdigit():
            print("Please enter only Integer number.")
            continue
        return int(value)


def read_range(description, start, end):
    """Accept a value and check that the number is within the predefined range."""
    while True:
        value = read_int(description)
        if value >= start and value <= end:
            return value
        print(f"The choice should be between [{start}, {end}]")
        continue


def get_customer_name(description: str) -> str:
    """Read and validate a customer's name."""
    while True:
        name = read_input(description)
        x = name.replace(" ", "")
        if not x.isalpha():
            print("That is not a correct name.")
            continue

        if 3 > len(name) > MAX_NAME_LEN:
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
        if not value.isdigit():
            print("Enter only an integer.")
            continue

        return value


def display_menu(menu):
    """Display the food menu in tabular format, grouped by category."""
    cat_no = 1
    for category, items in menu.items():
        print(f"\n-----------> {cat_no}. {category.upper()} <-----------\n")
        rows = []
        item_no = 1
        for item in items:
            rows.append(
                [item_no, item["name"], f"{item['price']} Birr", item["stock_quantity"]]
            )
            item_no += 1
        print(
            tabulate(
                rows, headers=["No", "Name", "Price", "Quantity"], tablefmt="fancy_grid"
            )
        )
        cat_no += 1


def select_food_category(description, categories=ALL_CATEGORIES, food_menu=food_menu):
    """Prompt the user to select a category after displaying the menu."""
    total_category = len(categories)
    temp = {}
    category_id = read_range(description, 1, total_category)
    category_id = category_id - 1  # normalize

    category = categories[category_id]
    print("Your choses are: ")
    temp[category] = food_menu[category]
    display_menu(temp)

    return category_id


def select_food_item(description, category_id, categories=ALL_CATEGORIES):
    """Prompt the user to select an item within the chosen category."""
    selected_category = categories[category_id]
    total_item_in_selected_category = len(food_menu[selected_category])
    item_id = read_range(description, 1, total_item_in_selected_category)
    return item_id - 1


# accepts value from select_food_category/item
def get_quantity(description, category_id, item_id):
    """Ask the user for a quantity, update stock, and return the selected amount."""
    category = food_menu[ALL_CATEGORIES[category_id]]
    selected_item = category[item_id]
    stock_quantity = selected_item["stock_quantity"]
    if stock_quantity >= 1:
        amount = read_range(description, 1, stock_quantity)
        selected_item["stock_quantity"] = stock_quantity - amount
        return amount
    return 0


# accepts amount from get_quantity
def check_stock(amount):
    """Return True if the requested amount is available, otherwise False."""
    return amount > 0


def get_price_each(category_id, item_id):
    """Return the price of the selected item."""
    category = food_menu[ALL_CATEGORIES[category_id]]
    selected_item = category[item_id]
    return selected_item["price"]


def calculate_subtotal(price, quantity):
    """Calculate the subtotal for a given price and quantity."""
    return price * quantity


##############
# CRUD OPERATION
##############
cart = {}


# add or update
def add_to_cart(category_id, item_id, amount):
    category = ALL_CATEGORIES[category_id]
    if category not in cart.keys() or (item_id not in cart[category]):
        cart[category] = []
        item = food_menu[category][item_id].copy()
        item["stock_quantity"] = amount
        item["price"] = get_price_each(category_id, item_id) * amount
        cart[category].append(item)
    else:
        item = food_menu[category][item_id].copy()
        new_price = get_price_each(category_id, item_id) * amount
        cart[category][item_id]["price"] += new_price
        cart[category][item_id]["stock_quantity"] += amount


def delete(catagory_prompt, item_prompt):
    categories = list(cart.keys())
    if categories == []:
        print("Please add some products first in order to delete")
        return False
    category_id = select_food_category(catagory_prompt, categories, food_menu=cart)

    item_id = select_food_item(item_prompt, category_id, categories)
    category = categories[category_id]
    item = cart[category][item_id]
    cart[category].remove(item)
    return True


def calculate_total():
    categories = list(cart.keys())
    total_price = 0
    for category, items in cart.items():
        category_id = categories.index(category)
        for i in items:
            item_id = cart[category].index("i")
            total_price += get_price_each(category_id, item_id)
    return total_price


def display_cart():
    display_menu(cart)


def test_display():
    while True:
        display_menu(food_menu)
        cat = select_food_category("Please select category: ")
        selected = ALL_CATEGORIES[cat]
        item = select_food_item(f"Please select food item from '{selected}' ", cat)

        selected = food_menu[selected][item]["name"]
        print(f"it seems you prefer {selected}\n okay now ,")
        amount = get_quantity("How much do you want: ", cat, item)

        print("selected amount: ", amount)
        check = check_stock(amount)  # check whether exist or not
        if not check:
            print("we finished that one choose other.")
            continue

        # check price
        price = get_price_each(cat, item)
        print("price is : ", price)
        print("which should be 60.")

        sub_total = calculate_subtotal(price, amount)
        print("sub total is ", sub_total)
        print("which is 120")

        add_to_cart(cat, item, amount)
        print(f"you want bought {amount} of {selected}s.\n\n\n\nYour order is now.\n")

        display_cart()

        # is_deleted = delete("Please enter category: ", "Please Enter item no: ")
        # print("Done!") if is_deleted else print("Faild to delete!")

        total = calculate_total()
        print("\n\n\n\n\ntotal price is : ", total)

        # price check
        # each_price = get_price_each(cat, item)
        # sub_total = calculate_subtotal(each_price, amount)


test_display()
