def get_cur_hedons():
    '''Return the number of hedons that the user has accumulated so far.
    '''
    global hedons
    return hedons


def get_cur_health():
    '''Return the number of health points that the user has accumulated so far.
    '''
    global health
    return health


def star_can_be_taken(activity):
    '''Return True iff a star can be used to get more hedons for activity 
    activity. A star can only be taken if no time passed between the star's 
    being offered and the activity, and the user is not bored with the stars, 
    and the star was offered for activity activity.
    '''
    global star
    global time
    global uninterested

    # check if the user has lost interest in stars and whether a star for
    # activity was just offered
    if len(star) > 0:
        if star[-1] == [time, activity]:
            if not uninterested:
                return True

    return False


def offer_star(activity):
    '''Simulate offering a star for engaging in the exercise activity.
    If three or more stars have beeen offered in the past three hours, set 
    uninterested to True to prevent any future stars from yielding bonus hedons.
    '''
    global star
    global uninterested

    star.append([time, activity])

    # if the user has not already lost interest in stars,
    # check if 3 stars have been offered in the past 2 hrs
    if not uninterested:
        counter = 0

        for i in reversed(star):
            if time - star[0][0] < 120:
                counter += 1

        if counter >= 3:
            uninterested = True


def is_tired():
    '''Return True iff running or textbooks has been performed in the last 120 
    mins, according to the activity_record.
    '''
    global activity_record

    for i in reversed(activity_record):
        if time - i[2] < 120:
            if i[0] == "running" or i[0] == "textbooks":
                return True

    return False


def minutes_ran_before():
    '''If the last activity performed was running, return the total time ran.
    Keep iterating through the activity record backwards until a time slot was not spent running.

    For instance:
    activity_record = [["resting", 30, 30], ["running", 60, 90]]
    minutes_ran_before() -> 60

    activity_record = [["resting", 30, 30], ["running", 60, 90], ["running", 20, 110]]
    minutes_ran_before() -> 80 (60 + 20)
    '''
    global activity_record

    total_time = 0

    for i in reversed(activity_record):
        if i[0] == "running":
            total_time += i[1]
        else:
            break

    return total_time


def perform_activity(activity, duration):
    '''Simulate the user performing activity for duration minutes.
    Allocate health points and hedons accordingly (based on tiredness, stars 
    and duration). Finally, add the activity to the activity_record.
    '''
    global health
    global hedons
    global time
    global activity_record

    if activity == "running":
        # check if using star
        using_star = star_can_be_taken("running")

        # allocate health points
        already_ran = 0

        if len(activity_record) > 0:
            # if the last activity was running, minutes ran in this time slot
            # will be added onto those already ran
            if activity_record[-1][0] == "running":
                already_ran = minutes_ran_before()

        for minute in range(1, duration + 1):
            if minute + already_ran > 180:
                health += 1
            else:
                health += 3

        # allocate hedons
        tired = is_tired()

        for minute in range(1, duration + 1):
            if tired:
                hedons -= 2
            else:
                if minute > 10:
                    hedons -= 2
                else:
                    hedons += 2

            if using_star and minute <= 10:
                hedons += 3

    elif activity == "textbooks":
        # check if using star
        using_star = star_can_be_taken("textbooks")

        # allocate health points
        health += 2 * duration

        # allocate hedons
        tired = is_tired()

        for minute in range(1, duration + 1):
            if tired:
                hedons -= 2
            else:
                if minute > 20:
                    hedons -= 1
                else:
                    hedons += 1

            if using_star and minute <= 10:
                hedons += 3

    elif activity == "resting":
        # allocate hedons
        if star_can_be_taken("resting"):
            hedons += 3 * duration
    else:
        return

    # add activity details to the activity record and increment time
    activity_record.append([activity, duration, time + duration])
    time += duration


def most_fun_activity_minute():
    '''Return the activity which would give 
    the most hedons if the person performed it 
    for one minute at the current time.
    '''
    running = 0
    textbooks = 0
    resting = 0

    tired = is_tired()

    # check "running" option
    using_star = star_can_be_taken("running")

    if tired:
        running -= 2
    else:
        running += 2

    if using_star:
        running += 3

    # check "textbooks" option
    using_star = star_can_be_taken("textbooks")

    if tired:
        textbooks -= 2
    else:
        textbooks += 1

    if using_star:
        textbooks += 3

    # check "resting" option
    using_star = star_can_be_taken("resting")

    if using_star:
        resting += 3

    # determine which activity yields maximum hedons
    if running > textbooks and running > resting:
        return "running"
    elif textbooks > running and textbooks > resting:
        return "textbooks"
    else:
        return "resting"


def initialize():
    '''Initialize the global variables needed for the simulation.
    '''
    # number of health points collected by the user
    global health
    # number of hedons collected by the user
    global hedons
    # time elapsed since beginning of simulation
    global time
    # a list containing each activity performed, the duration and the time
    # upon completion
    global activity_record
    # a list containing every instance a star was offered with the time and
    # activity for which it was offered
    global star
    # a boolean value describing whether the user has lost interest in stars
    global uninterested

    health = 0
    hedons = 0
    time = 0
    activity_record = []
    star = []
    uninterested = False


if __name__ == "__main__":
    initialize()
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("textbooks", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
