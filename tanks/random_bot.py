import random

def make_choice(x,y,field):
    actions = ["fire_up", "fire_down", "fire_left", "fire_right",
               "go_up","go_down","go_left","go_right"]
    return random.choice(actions)
