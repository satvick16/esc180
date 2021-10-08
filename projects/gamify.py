def get_cur_hedons():
    '''Return the number of hedons that 
    the user has accumulated so far.'''
    global hedons
    return hedons


def get_cur_health():
    '''Return the number of health points 
    that the user has accumulated so far.'''
    global health
    return health


def offer_star(activity):
    '''Simulate offering a star for 
    engaging in the exercise activity.'''
    global star

    star.append([time, activity])


def is_tired():
    global activity_record

    for i in reversed(activity_record):
        if time - i[1] < 120:
            if i[0] == "running" or i[0] == "textbooks":
                return True


def perform_activity(activity, duration):
    '''Simulate the user performing 
    activity for duration minutes.'''
    global health
    global hedons
    global time
    global star

    if activity == "running":
        # allocate health points
        if duration > 180:
            health += 180 * 3
            health += duration - 180
        else:
            health += 3 * duration

        # allocate hedons
        if is_tired():
            hedons -= 2 * duration
        else:
            if duration > 10:
                hedons += 2 * duration
                hedons -= 2 * (duration - 10)
            else:
                hedons += 2 * duration
    elif activity == "textbooks":
        # allocate health points
        health += 2 * duration

        # allocate hedons
        if is_tired():
            hedons -= 2 * duration
        else:
            if duration > 20:
                hedons += duration
                hedons -= duration - 20
            else:
                hedons += duration
    elif activity == "resting":
        pass
    else:
        return

    activity_record.append([activity, time + duration])
    time += duration


def star_can_be_taken(activity):
    '''Return True iff a star can be used 
    to get more hedons for activity activity. 
    A star can only be taken if no time passed 
    between the star's being offered ans the 
    activity, and the user is not bored with 
    the stars, and the star was offered for 
    activity activity.'''
    pass


def most_fun_activity_minute():
    '''Return the activity which would give 
    the most hedons if the person performed it 
    for one minute at the current time.'''
    pass


def initialize():
    '''Initializes the global variables needed for 
    the simulation. Note: this function is incomplete, 
    and you may want to modify it'''
    global health
    global hedons
    global time
    global activity_record
    global star

    health = 0
    hedons = 0
    time = 0
    activity_record = []
    star = []


if __name__ == "__main__":
    initialize()
    perform_activity("running", 30)
    # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_hedons())
    # 90 = 30 * 3                          # Test 2
    print(get_cur_health())
    # resting                              # Test 3
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    offer_star("running")
    # running                              # Test 4
    print(most_fun_activity_minute())
    perform_activity("textbooks", 30)
    # 150 = 90 + 30*2                      # Test 5
    print(get_cur_health())
    # -80 = -20 + 30 * (-2)                # Test 6
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 20)
    # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_health())
    # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    print(get_cur_hedons())
    perform_activity("running", 170)
    # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_health())
    # -430 = -90 + 170 * (-2)              # Test 10
    print(get_cur_hedons())
