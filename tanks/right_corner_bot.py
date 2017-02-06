import random


def make_choice(x, y, field):
    x_size = len(field)
    y_size = len(field[0])

    if x < x_size - 1:
        return "go_right"
    if y < y_size - 1:
        return "go_down"

    return random.choice(["fire_up", "fire_left"])