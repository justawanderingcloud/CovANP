import random


def select():
    test_list = ["first", "second", "third"]
    random_selected = random.sample(test_list, 1)[0]
    return random_selected
