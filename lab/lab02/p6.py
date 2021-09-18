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


def memory():
    global current_value
    global saved

    save = current_value


def recall():
    global current_value
    global saved

    current_value = saved


if __name__ == "__main__":
    current_value = 0
    saved = 0
    display_current_value()  # 0
    memory()  # save 0
    add(3)  # add 3 to current_value
    display_current_value()  # 3
    recall()  # reset current_value to 0
    display_current_value()  # 0
