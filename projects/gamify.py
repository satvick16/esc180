def perform_activity(activity, minutes):
    global health

    if activity == "running":
        if minutes > 180:
            health += minutes -
        else:
            pass
    elif activity == "textbooks":
        health += minutes * 2


def get_cur_hedons():
    global hedons
    return hedons


def get_cur_health():
    global health
    return health


def initialize():
    global health
    global hedons

    health = 0
    hedons = 0


if __name__ == "__main__":
    health = 0
    hedons = 0
