# return ok if username matches password
# if there are 3 failed attempts, return refused

def login(username, password):
    global n_attempts

    if n_attempts >= 3:
        n_attempts += 1

        return "refused"

    if username == "acharya" and password == "python":
        n_attempts = 0
        return "ok"
    if username == "stangeby" and password == "rigorous":
        n_attempts = 0
        return "ok"

    n_attempts += 1

    return "refused"


def initialize():
    global n_attempts
    n_attempts = 0
