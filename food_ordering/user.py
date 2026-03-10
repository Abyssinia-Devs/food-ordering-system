MAX_NAME_LEN = 20
PHONE_NUM_LEN = 10
PHONE_NUM_BEGIN = "09"


def read_input(description: str) -> str:
    return input(description).strip()


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

        if not value.isdigit():
            print("Please enter only numbers.")
            continue

        return value