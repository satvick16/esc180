def try_(input):
    global past_inputs

    if input != "pumpkin":
        past_inputs.append(input)
        return "locked"
    else:
        if len(past_inputs) >= 3:
            if past_inputs[len(past_inputs)-3:] == ["fall", "costumes", "costumes"]:
                past_inputs.append(input)
                return "unlocked"
        past_inputs.append(input)
        return "locked"


if __name__ == "__main__":
    past_inputs = []

    print(try_("ghosts"))
    print(try_("leaves"))
    print(try_("fall"))
    print(try_("costumes"))
    print(try_("costumes"))
    print(try_("pumpkin"))
    print(try_("pumpkin"))
    print(try_("fall"))
    print(try_("costumes"))
    print(try_("costumes"))
    print(try_("pumpkin"))
    print(try_("fall"))
