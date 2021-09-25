def display_current_value():
    print(f"Current value: {current_value}")


def add(to_add):
    global current_value
    global past_value
    past_value = current_value
    current_value += to_add


def multiply(to_multiply):
    global current_value
    global past_value
    past_value = current_value
    current_value *= to_multiply


def subtract(to_subtract):
    add(-1 * to_subtract)


def divide(to_divide):
    # issue: zero division
    if to_divide == 0:
        print("ERROR! Cannot divide by zero.")
    else:
        multiply(1 / to_divide)


def memory():
    global current_value
    global memory_value

    memory_value = current_value


def recall():
    global current_value
    global memory_value

    current_value = memory_value


def undo():
    global current_value
    global past_value
    temp = current_value
    current_value = past_value
    past_value = temp
