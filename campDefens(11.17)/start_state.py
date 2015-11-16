import game_framework
import frist_stage
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1000,600)
    image = load_image('image\\kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(frist_stage)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(500, 300, 1000, 600)
    update_canvas()




def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass




