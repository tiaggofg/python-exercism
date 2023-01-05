EXPECTED_BAKE_TIME = 40


def bake_time_remaining(time_in_the_oven):
    """
    This function takes a time has been lasagna is the oven and return
    how many minutes lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

    :param time_in_the_oven:
    :return: bake time remaining
    """

    return EXPECTED_BAKE_TIME - time_in_the_oven


def preparation_time_in_minutes(steps):
    """
    This function takes the number of necessary steps to cook a lasagna
    and returns how many minutes you would spend making them

    :param steps:
    :return: lasagna cooking time
    """

    return steps * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.

    :param number_of_layers:
    :param elapsed_bake_time:
    :return: elapsed cooking time
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
