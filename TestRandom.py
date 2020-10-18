import random


def select(howmany):
    test_list = ["first", "second", "third"]
    random_selected = random.sample(test_list, howmany) #[0]
    print(random_selected)
    # return random_selected
