import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
bgm = None
logo_time = 0.0


def enter():
    global image
    global bgm
    image = load_image('image\\end_background.png')
    bgm = load_music('sound\\ending.mp3')
    bgm.set_volume(50)
    bgm.repeat_play()

def exit():
    global image
    global bgm
    del(image)
    del(bgm)

def update(frame_time):
    global logo_time

    if(logo_time > 5.0):
        logo_time = 0
        game_framework.push_state(title_state)
    logo_time += frame_time


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




