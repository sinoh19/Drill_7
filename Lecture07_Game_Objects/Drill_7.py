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

    def update(self):
        if self.y > self.size:
            self.y -= self.size
            if self.y < self.size:
                self.y = self.size # 바닥에 닿으면 멈춤

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
    pass

def rest_world():
    global running
    global grass
    global balls

    running = True
    grass = Grass()
    balls = [Ball() for i in range(20)]

def update_world():
    grass.update()
    for ball in balls:
        ball.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

open_canvas()