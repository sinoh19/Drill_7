from pico2d import *
import random


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
    running = True

def update_world():
    pass

def render_world():
    clear_canvas()
    update_canvas()
    open_canvas()
    rest_world()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()



close_canvas()
