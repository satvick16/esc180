def display_current_value():
    print(f"Current value: {current_value}")


def add(to_add):
    global current_value
    current_value += to_add


def multiply(to_multiply):
    global current_value
    current_value *= to_multiply


def divide(to_divide):
    # issue: zero division
    global current_value
    current_value /= to_divide


if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(5)
    display_current_value()
