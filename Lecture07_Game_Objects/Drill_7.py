from pico2d import *
import random


class Ball:
    def __init__(self):
        if random.randint(0,1) == 0:
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41

        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
