def display_current_value():
    global current_value
    print(current_value)


def add(to_add):
    global current_value
    global prev
    prev = current_value
    current_value += to_add


def subtract(to_subtract):
    global current_value
    global prev
    prev = current_value
    add(-1 * to_subtract)


def mult(to_multiply):
    global current_value
    global prev
    prev = current_value
    current_value *= to_multiply


def divide(to_divide):
    global current_value
    global prev
    prev = current_value
    if to_divide == 0:
        return
    mult(1 / to_divide)


def memory():
    global current_value
    global memory
    memory = current_value


def recall():
    global current_value
    global memory
    current_value = memory


def undo():
    global current_value
    global prev
    current_value, prev = prev, current_value


if __name__ == "__main__":
    current_value = 0
    memory = 0
    prev = 0

    display_current_value()  # 0
    add(5)  # 5
    subtract(2)
    display_current_value()  # 3
    undo()
    display_current_value()  # 5
    undo()
    display_current_value()  # 3
    mult(10)
    display_current_value()  # 30
    undo()
    undo()
    display_current_value()  # 30
    undo()
    undo()
    undo()
    display_current_value()  # 3
