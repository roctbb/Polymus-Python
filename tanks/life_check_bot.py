import random

def make_choice(x ,y ,field):
    if field[x][y]["life" ] >5:
        return random.choice(["fire_up", "fire_down" ,"fire_left", "fire_right"])
    else:
        return random.choice(["go_up", "go_down", "go_left", "go_right"])