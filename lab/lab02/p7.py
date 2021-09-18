def display_current_value():
    print(f"Current value: {current_value}")


def add(to_add):
    global current_value
    current_value += to_add
    global past_values
    past_values.append(current_value)


def multiply(to_multiply):
    global current_value
    current_value *= to_multiply
    global past_values
    past_values.append(current_value)


def subtract(to_subtract):
    add(-1 * to_subtract)


def divide(to_divide):
    # issue: zero division
    multiply(1 / to_divide)


def memory():
    global current_value

    with open("test.txt", "w") as f:
        f.write(str(current_value))


def recall():
    global current_value

    with open("test.txt", "r") as f:
        current_value = int(f.read())


def undo():
    global current_value
    global past_values
    current_value = past_values[-2]
    past_values.append(current_value)


if __name__ == "__main__":
    current_value = 0
    past_values = [0]
    display_current_value()  # 0
    add(5)  # 5
    subtract(2)
    display_current_value()  # 3
    undo()
    display_current_value()  # 5
    undo()
    display_current_value()  # 3
    multiply(10)
    display_current_value()  # 30
    undo()
    undo()
    display_current_value()  # 30
    undo()
    undo()
    undo()
    display_current_value()  # 3
